class CoordinatorAgent:

    def make_final_decision(self, demand_result, supplier_result, inventory_result, logistics_result):

        risk_colors = [
            demand_result["color"],
            supplier_result["color"],
            inventory_result["color"],
            logistics_result["color"]
        ]

        if "Red" in risk_colors:
            final_status = "Critical"
            final_color = "Red"
            final_decision = (
                "High disruption risk detected. Use backup supplier, increase reorder quantity, "
                "and choose faster logistics route."
            )

        elif "Orange" in risk_colors:
            final_status = "Moderate"
            final_color = "Orange"
            final_decision = (
                "Moderate risk detected. Monitor supplier, maintain safety stock, "
                "and keep logistics buffer."
            )

        else:
            final_status = "Stable"
            final_color = "Green"
            final_decision = (
                "Supply chain condition is stable. Continue normal operations."
            )

        return {
            "final_status": final_status,
            "final_color": final_color,
            "final_decision": final_decision,
            "demand_result": demand_result,
            "supplier_result": supplier_result,
            "inventory_result": inventory_result,
            "logistics_result": logistics_result
        }