# Copyright (c) 2021, Mitja Karhusaari <mitja.karhusaari@helsinki.fi> and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import functools
import pymysql
import pymysql.cursors

def with_connection(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        with self.connect() as conn:
            with conn.cursor() as cur:
                return method(self, cur, *args, **kwargs)
    
    return wrapper

class MembersIntegrationSettings(Document):
    def connect(self):
        password = self.get_password('db_password')

        return pymysql.connect(
            host=self.db_host,
            user=self.db_user,
            port=self.db_port or 3306,
            password=password,
            database=self.db_name,
            cursorclass=pymysql.cursors.DictCursor,
        )

    def test_connection(self):
        try:
            self.connect()
        except:
            return dict(success=False)

        return dict(success=True)

    @with_connection
    def sync_members(self, cursor):
        successful = 0
        failed = 0

        cursor.execute("SELECT * FROM users")
        
        for row in cursor.fetchall():
            try:
                self.update_member_data(row)
                successful += 1
            except:
                failed += 1

        return dict(failed=failed, successful=successful)

    @with_connection
    def sync_single(self, cursor, username, **kwargs):
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        row = cursor.fetchone()
        self.update_member_data(row, **kwargs)

    def update_member_data(self, data, **kwargs):
        member = None

        if frappe.db.exists('Member', data['username']):
            member = frappe.get_doc('Member', data['username'])
        else:
            member = frappe.new_doc('Member')

        member.username = data['username']
        member.email = data['email']
        member.role = data['role']
        member.real_name = data['name']
        member.screen_name = data['screen_name']
        member.membership = data['membership']
        member.phone = data['phone']

        member.save(**kwargs)
        
    def get_user_service_url(self, path='/'):
        return f'{self.user_service_public_url}{path}?serviceIdentifier={self.user_service_id}'
