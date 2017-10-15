
from __future__ import unicode_literals
import frappe

def after_install():
	from frappe.custom.doctype.custom_field.custom_field import create_custom_field
	create_custom_field('School Settings', {
		'label': ('School Type'),
		'fieldname': 'school_type',
		'fieldtype': 'Data',
		'default': "Pri",
		'insert_after': 'validate_course'
	})	

	frappe.db.set_value("School Settings", "School Settings", "school_type", "Pri")