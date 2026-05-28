import joblib
import pandas as pd

class DemandAgent:

    def __init__(self):
        self.model = joblib.load("models/demand_forecasting_model.pkl")

    def predict_demand(self, input_data):
        df = pd.DataFrame([input_data])
        prediction = self.model.predict(df)[0]

        if prediction > 7000:
            level = "High"
            color = "Red"
        elif prediction > 4000:
            level = "Medium"
            color = "Orange"
        else:
            level = "Low"
            color = "Green"

        return {
            "predicted_demand": prediction,
            "demand_level": level,
            "color": color
        }