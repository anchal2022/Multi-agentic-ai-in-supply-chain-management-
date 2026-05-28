import joblib
import pandas as pd

class SupplierRiskAgent:

    def __init__(self):
        self.model = joblib.load("models/supplier_risk_model.pkl")

    def predict_supplier_risk(self, input_data):
        df = pd.DataFrame([input_data])
        prediction = self.model.predict(df)[0]

        if prediction == "High":
            color = "Red"
            action = "Avoid this supplier or use backup supplier."
        elif prediction == "Medium":
            color = "Orange"
            action = "Monitor supplier and keep safety stock."
        else:
            color = "Green"
            action = "Supplier is safe to use."

        return {
            "supplier_risk_level": prediction,
            "color": color,
            "recommended_action": action
        }