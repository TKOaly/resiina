import frappe
import pymysql

@frappe.whitelist()
def sync_members():
    settings = frappe.get_single("Members Integration Settings")
    return settings.sync_members()

def sync_single_member(username):
    settings = frappe.get_single("Members Integration Settings")
    settings.sync_single(username, ignore_permissions=True)

@frappe.whitelist()
def test_members_connection():
    settings = frappe.get_single("Members Integration Settings")
    return settings.test_connection()

@frappe.whitelist(allow_guest=True)
def get_user_service_url():
    settings = frappe.get_single("Members Integration Settings")
    return settings.get_user_service_url()

