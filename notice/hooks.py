from . import __version__ as app_version

app_name = "notice"
app_title = "Notice"
app_publisher = "Diya"
app_description = "Notice Board"
app_email = "notice@gmail.com"
app_license = "n"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/notice/css/notice.css"
# app_include_js = "/assets/notice/js/notice.js"

# include js, css files in header of web template
# web_include_css = "/assets/notice/css/notice.css"
# web_include_js = "/assets/notice/js/notice.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "notice/public/scss/website"

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
#	"methods": "notice.utils.jinja_methods",
#	"filters": "notice.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "notice.install.before_install"
# after_install = "notice.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "notice.uninstall.before_uninstall"
# after_uninstall = "notice.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "notice.utils.before_app_install"
# after_app_install = "notice.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "notice.utils.before_app_uninstall"
# after_app_uninstall = "notice.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "notice.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"notice.tasks.all"
#	],
#	"daily": [
#		"notice.tasks.daily"
#	],
#	"hourly": [
#		"notice.tasks.hourly"
#	],
#	"weekly": [
#		"notice.tasks.weekly"
#	],
#	"monthly": [
#		"notice.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "notice.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "notice.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "notice.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["notice.utils.before_request"]
# after_request = ["notice.utils.after_request"]

# Job Events
# ----------
# before_job = ["notice.utils.before_job"]
# after_job = ["notice.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"notice.auth.validate"
# ]
