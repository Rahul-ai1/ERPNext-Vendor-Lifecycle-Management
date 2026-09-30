# Copyright (c) 2026, Rahul Chaudhary and contributors
# For license information, please see LICENSE

import frappe


def execute():
	from vendor_lifecycle.vendor_lifecycle.install import (
		backfill_default_signoff_renewal_email_templates,
	)

	backfill_default_signoff_renewal_email_templates()
