import frappe
import frappe.handler
import functools
import os

__version__ = '0.0.1'

def wrap_logout(func):
    @functools.wraps(func)
    @frappe.whitelist(allow_guest=True)
    def wrapper():
        func()

        settings = frappe.get_single("Members Integration Settings")
        url = settings.get_user_service_url('/logout')

        if 'token' in frappe.request.cookies:
            frappe.local.response['type'] = 'redirect'
            frappe.local.response['location'] = url

    return wrapper

frappe.handler.web_logout = wrap_logout(frappe.handler.web_logout)
frappe.handler.logout = wrap_logout(frappe.handler.logout)
