import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error, accuracy_score, f1_score
import numpy as np

df = pd.read_csv("dataset/processed/final_pcb_scm_dataset.csv")

# -----------------------------
# Model 1: Demand Forecasting
# -----------------------------
X_demand = df[["month", "lead_time_days", "shipping_time_days", "opening_stock_units", "planned_order_units"]]
y_demand = df["actual_demand_units"]

X_train, X_test, y_train, y_test = train_test_split(X_demand, y_demand, test_size=0.2, random_state=42)

demand_model = RandomForestRegressor(random_state=42)
demand_model.fit(X_train, y_train)

demand_pred = demand_model.predict(X_test)

mae = mean_absolute_error(y_test, demand_pred)
rmse = np.sqrt(mean_squared_error(y_test, demand_pred))

# -----------------------------
# Model 2: Supplier Delay Risk
# -----------------------------
X_risk = df[["lead_time_days", "supplier_delay_days", "shipping_time_days", "disruption_severity_1_to_5"]]
y_risk = df["risk_level"]

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_risk, y_risk, test_size=0.2, random_state=42)

risk_model = RandomForestClassifier(random_state=42)
risk_model.fit(X_train_r, y_train_r)

risk_pred = risk_model.predict(X_test_r)

accuracy = accuracy_score(y_test_r, risk_pred)
f1 = f1_score(y_test_r, risk_pred, average="weighted")

# Save models
os.makedirs("models", exist_ok=True)
joblib.dump(demand_model, "models/demand_forecasting_model.pkl")
joblib.dump(risk_model, "models/supplier_risk_model.pkl")

# Save results
os.makedirs("paper_results", exist_ok=True)

results = pd.DataFrame({
    "Model": ["Demand Forecasting", "Supplier Risk Classification"],
    "Metric 1": ["MAE", "Accuracy"],
    "Value 1": [mae, accuracy],
    "Metric 2": ["RMSE", "F1-score"],
    "Value 2": [rmse, f1]
})

results.to_csv("paper_results/ml_model_results.csv", index=False)

print("✅ ML model training completed")
print(results)