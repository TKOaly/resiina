import frappe
from frappe.utils import datetime
import jwt
import requests
import os
from resiina.integration import sync_single_member

def extend_bootinfo(bootinfo):
    pass

def validate_session():
    token = frappe.request.cookies.get('token')

    if not token:
        return

    settings = frappe.get_single('Members Integration Settings')
    jwt_secret = settings.get_password('user_service_secret')

    try:
        jwt.decode(token, key=jwt_secret, algorithms=['HS256'])
    except Exception as e:
        return

    cache_key = 'resiina:members-token:' + token

    user = frappe.cache().get(cache_key)

    if not user:
        user = update_user_into(token, settings)
        frappe.cache().set(cache_key, user)
    else:
        user = user.decode('utf-8')

    login = frappe.auth.LoginManager()
    login.user = user
    login.post_login()

def update_user_into(token, settings):
    user_service_url = settings.user_service_internal_url
    service_identifier = settings.user_service_id

    res = requests.get(
        f'{user_service_url}/api/users/me?dataRequest=535',
        headers={
            "Authorization": f"Bearer {token}",
            "Service": service_identifier,
        },
    )

    data = res.json()['payload']

    user = None

    if not frappe.db.exists('User', data['email']):
        print('Creating User')
        user = frappe.new_doc("User")
        user.flags.ignore_permissions = True
        user.flags.send_welcome_email = False
        update_user_info(user, data)
        user.save()
    else:
        user = frappe.get_doc('User', data['email'])
        user.flags.ignore_permissions = True
        update_user_info(user, data)
        user.save()

    if not frappe.db.exists('Member', data['username']):
        sync_single_member(data['username'])

    member = frappe.get_doc('Member', data['username'])
    member.user = data.get('email')
    member.flags.ignore_permissions = True
    member.save()

    frappe.db.commit()

    return user.name

ROLE_MAP = {
    'yllapitaja': ('System User', ['Administrator']),
    'virkailija': ('System User', ['Officer']),
    'jasenvirkailija': ('System User', ['Officer', 'Member Coordniator']),
}

def update_user_info(user, data):
    user.email = data.get("email")
    user.username = data.get('username')
    user.first_name = data["name"].rsplit(" ", 1)[0]
    user.last_name = data["name"].rsplit(" ", 1)[1]

    user_type, roles = ROLE_MAP.get(data['role'], ('Website User', []))

    user.user_type = user_type
    user.add_roles(*roles)

def on_logout():
    pass
