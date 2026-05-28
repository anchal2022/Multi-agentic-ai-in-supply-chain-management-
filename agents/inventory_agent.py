class InventoryAgent:

    def check_inventory(self, input_data):
        stock = input_data["opening_stock_units"]
        reorder_point = input_data["reorder_point_units"]
        demand = input_data["actual_demand_units"]

        if stock < reorder_point:
            status = "Low Stock"
            color = "Red"
            action = "Place reorder immediately."
        elif stock < demand:
            status = "Medium Stock"
            color = "Orange"
            action = "Monitor inventory and prepare reorder."
        else:
            status = "Safe Stock"
            color = "Green"
            action = "Inventory level is sufficient."

        reorder_quantity = max(0, demand - stock)

        return {
            "inventory_status": status,
            "reorder_quantity": reorder_quantity,
            "color": color,
            "recommended_action": action
        }