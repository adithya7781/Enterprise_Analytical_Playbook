import pandas as pd

df = pd.read_csv("../data/output/hospital_master_elt.csv")

# --------------------------------
# Business Rule
# --------------------------------

high_priority = df[
    (df["total_amount"] > 50000) &
    (df["payment_status"] == "Pending")
]

high_priority.to_csv(
    "../data/output/high_priority_patients.csv",
    index=False
)

print("="*50)
print("Reverse ETL Completed Successfully")
print("="*50)

print("Patients exported :", len(high_priority))