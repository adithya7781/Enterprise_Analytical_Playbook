

<h2 align="center">
  ETL vs ELT vs Reverse ETL</h2>

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Transformation-CC2927?logo=mysql&logoColor=white)
![Healthcare](https://img.shields.io/badge/Domain-Healthcare-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

> End-to-end implementation of **ETL, ELT, and Reverse ETL** using a Hospital Management dataset to simulate a real-world healthcare analytics workflow.

---

# Project Overview

This project demonstrates how operational hospital data can be transformed into analytics-ready datasets and then pushed back into business operations using modern data engineering concepts.

The implementation covers the complete lifecycle:

- Data Discovery
- ETL Pipeline
- ELT Pipeline
- Reverse ETL

---

# Repository Structure

```text
01_ETL_ELT_Reverse_ETL/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── output/
│
├── scripts/
│   ├── 01_data_discovery.py
│   ├── etl_pipeline.py
│   ├── elt_pipeline.py
│   └── reverse_etl.py
│
├── images/
│   ├── project_cover.png
│   ├── etl_architecture.png
│   ├── elt_architecture.png
│   ├── reverse_etl_architecture.png
│   └── workflow.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Dataset

## Domain

Healthcare

## Description

The Hospital Management dataset contains **18 normalized relational tables** representing various hospital operations.

### Major Tables

- Patient
- Admission
- Billing
- Billing Detail
- Department
- Doctor
- Disease
- Drug
- Prescription
- Employee
- Insurance Provider
- Patient Insurance
- Patient Diagnostic
- Ward
- Bed
- Drug Inventory
- Drug Manufacturer
- Staff Assignment

---

# Data Discovery

Before implementing the pipelines, automated profiling was performed.

### Data Profiling

- Total Tables: **18**
- Duplicate Detection
- Missing Value Analysis
- Data Type Validation
- Relationship Identification
- Master vs Transaction Table Analysis

---

# ETL Pipeline

## Extract

Loaded raw hospital CSV files using Pandas.

## Transform

- Removed duplicate records
- Standardized column names
- Converted date columns
- Trimmed text values
- Merged multiple relational tables
- Prepared analytics-ready data

## Load

Generated

```text
hospital_master.csv
```

---

# ELT Pipeline

## Extract

Loaded raw CSV files.

## Load

Imported data directly into SQLite.

## Transform

Performed SQL transformations inside the database using:

- LEFT JOIN
- COALESCE
- SQL-based Integration

Generated

```text
hospital.db

hospital_master_elt.csv
```

---

# Reverse ETL

Business Rule

```text
Total Amount > ₹50,000

AND

Payment Status = Pending
```

Generated

```text
high_priority_patients.csv
```

This dataset simulates exporting analytical insights back to operational systems for business action.

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Data Processing |
| Pandas | ETL |
| SQLite | ELT |
| SQL | Data Transformation |
| Git | Version Control |

---

# Project Outputs

| Output | Description |
|---------|-------------|
| hospital_master.csv | ETL Output |
| hospital.db | SQLite Database |
| hospital_master_elt.csv | ELT Output |
| high_priority_patients.csv | Reverse ETL Output |

---

# Business Value

This project demonstrates how healthcare organizations can:

- Consolidate operational data
- Prepare analytics-ready datasets
- Perform SQL transformations inside a database
- Identify high-priority patients using business rules
- Deliver analytical insights back to operational teams

---

# Skills Demonstrated

- Data Discovery
- Data Profiling
- ETL
- ELT
- Reverse ETL
- SQL Joins
- Data Cleaning
- Data Integration
- SQLite
- Healthcare Analytics

---

# Author

**Ketharaju Vishal Adithya**

Data Analytics | Business Intelligence | SQL | Python | Power BI | AI

GitHub: https://github.com/adithya7781

LinkedIn: https://www.linkedin.com/in/vishal-adithya-381012276

Portfolio: https://artfolio.tech/VishalAdithya
