import json
import frappe

@frappe.whitelist()
def create_warehouse(self, method=None):
    self=json.loads(self)
    warehouse_detail=frappe.get_doc("Warehouse",self.get("name"))
    if warehouse_detail == null:
        new_warehouse = frappe.new_doc("Warehouse")
        new_warehouse.warehouse_name = self.get("cost_center_name")
        new_warehouse.custom_cost_center = self.get("name")
        new_warehouse.insert()


@frappe.whitelist()
def fetch_all_cost_centers():
    cost_centers = frappe.get_all("Cost Center", fields=["name"])
    return cost_centers
