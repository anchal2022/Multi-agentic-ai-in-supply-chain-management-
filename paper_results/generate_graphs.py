import pandas as pd
import matplotlib.pyplot as plt
import os

# Load KPI summary
df = pd.read_csv("paper_results/kpi_summary.csv")

os.makedirs("paper_results/graphs", exist_ok=True)

# Plot each KPI comparison
for i in range(len(df)):
    kpi = df.loc[i, "KPI"]
    baseline = df.loc[i, "Baseline"]
    proposed = df.loc[i, "Proposed_Multi_Agent_AI"]

    plt.figure()
    plt.bar(["Baseline", "Proposed"], [baseline, proposed])
    plt.title(kpi)
    plt.ylabel("Value")

    plt.savefig(f"paper_results/graphs/{kpi.replace(' ', '_')}.png")
    plt.close()

print("✅ Graphs generated successfully")