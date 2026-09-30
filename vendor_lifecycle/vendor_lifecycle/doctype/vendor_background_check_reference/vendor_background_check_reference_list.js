// Copyright (c) 2026, Rahul Chaudhary and contributors
// For license information, please see LICENSE

frappe.listview_settings["Vendor Background Check Reference"] = {
	refresh(listview) {
		// References only ever make sense linked to a Background Check —
		// the list view's own "Add" button is hidden so the "Create
		// Reference" button on Vendor Background Check stays the one way
		// to create one.
		listview.can_create = false;
		listview.page.clear_primary_action();
	},
};
