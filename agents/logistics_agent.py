class LogisticsAgent:

    def check_logistics(self, input_data):
        shipping_time = input_data["shipping_time_days"]
        logistics_cost = input_data["logistics_cost_usd"]
        delay_flag = input_data["delay_flag"]

        if delay_flag == 1 or shipping_time > 20:
            status = "High Delay Risk"
            color = "Red"
            action = "Use faster route or alternate logistics partner."
        elif shipping_time > 10:
            status = "Medium Delay Risk"
            color = "Orange"
            action = "Monitor shipment and keep buffer time."
        else:
            status = "Low Delay Risk"
            color = "Green"
            action = "Logistics plan is normal."

        return {
            "logistics_status": status,
            "shipping_time_days": shipping_time,
            "logistics_cost_usd": logistics_cost,
            "color": color,
            "recommended_action": action
        }