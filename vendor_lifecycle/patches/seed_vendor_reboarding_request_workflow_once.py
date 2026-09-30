# Copyright (c) 2026, Rahul Chaudhary and contributors
# For license information, please see LICENSE

import frappe


def execute():
	# Same reasoning as seed_vendor_kyc_workflow_once.py - a separate,
	# one-time patch so a deliberate later change to this Workflow (through
	# the Workflow Builder, or a deletion) actually sticks rather than
	# being silently reverted on every migrate.
	from vendor_lifecycle.vendor_lifecycle.install import install_vendor_reboarding_request_workflow

	install_vendor_reboarding_request_workflow()
