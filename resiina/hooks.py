from . import __version__ as app_version

app_name = "resiina"
app_title = "Resiina"
app_publisher = "Mitja Karhusaari <mitja.karhusaari@helsinki.fi>"
app_description = "An app for TKO-äly\'s needs."
app_icon = "octicon octicon-file-directory"
app_color = "orange"
app_email = "-"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/resiina/css/resiina.css"
# app_include_js = "/assets/resiina/js/resiina.js"

# include js, css files in header of web template
web_include_css = [
    "/assets/resiina/css/members_login_button.css"
]
web_include_js = [
    "/assets/resiina/js/members_login_button.js"
]

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "resiina/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "resiina.utils.jinja_methods",
# 	"filters": "resiina.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "resiina.install.before_install"
# after_install = "resiina.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "resiina.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
    "daily": ["resiina.integration.sync_members"],
}

# scheduler_events = {
# 	"all": [
# 		"resiina.tasks.all"
# 	],
# 	"daily": [
# 		"resiina.tasks.daily"
# 	],
# 	"hourly": [
# 		"resiina.tasks.hourly"
# 	],
# 	"weekly": [
# 		"resiina.tasks.weekly"
# 	],
# 	"monthly": [
# 		"resiina.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "resiina.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "resiina.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "resiina.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

extend_bootinfo = [
    "resiina.integration.auth.extend_bootinfo"
]

auth_hooks = [
    "resiina.integration.auth.validate_session"
]

on_logout = [
    "resiina.integration.auth.on_logout"
]

# auth_hooks = [
# 	"resiina.auth.validate"
# ]

