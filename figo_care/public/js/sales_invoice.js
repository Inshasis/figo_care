// Copyright (c) 2024, InshaSiS Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sales Invoice', {
	refresh(frm) {
	    frm.add_custom_button(__('Make Payment Entry'), function(){
            frappe.call({
            method:"figo_care.figo_care.doctype.sales_invoice.cash_payment_action",
            args:{
                doc:cur_frm.doc,
            },
            callback:function(r){
                console.log("*************** Payment Entry Created *******************");
            }
            });
        }).css({ 'background-color': '#10a139', 'color': 'white' });
	}
});