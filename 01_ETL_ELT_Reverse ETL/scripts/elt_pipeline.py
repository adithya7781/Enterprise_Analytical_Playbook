import os
import sqlite3
import pandas as pd

RAW_PATH = "../data/raw"
DB_PATH = "../data/output/hospital.db"

conn = sqlite3.connect(DB_PATH)

tables = [
    "patient",
    "admission",
    "department",
    "billing",
    "disease"
]

# --------------------------
# EXTRACT + LOAD
# --------------------------

for table in tables:

    df = pd.read_csv(f"{RAW_PATH}/{table}.csv")

    df.to_sql(
        table,
        conn,
        if_exists="replace",
        index=False
    )

print("Raw tables loaded into database.")

# --------------------------
# TRANSFORM
# --------------------------

query = """

CREATE TABLE hospital_master AS

SELECT

p.patient_id,
p.gender,
p.city,

a.admission_date,
a.discharge_date,

COALESCE(d.department_name, 'Unknown') AS department_name,

COALESCE(ds.disease_name, 'Unknown') AS disease_name,

COALESCE(b.total_amount, 0) AS total_amount,

COALESCE(b.payment_status, 'Not Available') AS payment_status

FROM patient p

LEFT JOIN admission a
ON p.patient_id = a.patient_id

LEFT JOIN department d
ON a.department_id = d.department_id

LEFT JOIN disease ds
ON a.disease_id = ds.disease_id

LEFT JOIN billing b
ON a.admission_id = b.admission_id;

"""

conn.execute("DROP TABLE IF EXISTS hospital_master")
conn.execute(query)

df = pd.read_sql("SELECT * FROM hospital_master", conn)

df.to_csv("../data/output/hospital_master_elt.csv", index=False)

conn.close()

print("="*50)
print("ELT Completed Successfully")
print("="*50)

print(df.head())