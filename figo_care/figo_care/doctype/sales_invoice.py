# Copyright (c) 2023, envisionx Oman and contributors
# For license information, please see license.txt

import json
import frappe


# Cash Payment
@frappe.whitelist()
def cash_payment_action(doc):
    doc = json.loads(doc)
    pe = frappe.get_doc({
        "doctype": "Payment Entry",
        "payment_type" : "Receive",
        "mode_of_payment" : "Cash",
        "company" : doc.get("company"),
        "cost_center" : doc.get("cost_center"),
        "posting_date" : doc.get("posting_date"),
        "party_type" : "Customer",
        "party" : doc.get("customer"),
        "paid_to" : "1110 - Cash - FCPL",
        "paid_amount" : doc.get("rounded_total"),
        "received_amount" : doc.get("rounded_total"),
    })    
    pe.append("references",{
        "reference_doctype":"Sales Invoice",
        "reference_name":doc.get("name"),
        "allocated_amount":doc.get("rounded_total"),
    })   
    pe.insert()
    pe.submit()
    frappe.msgprint("Created Payment Entry Successfull")
