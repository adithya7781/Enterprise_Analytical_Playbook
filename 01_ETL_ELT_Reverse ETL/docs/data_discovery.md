# Data Discovery Report

## Overview

Before implementing the ETL, ELT, and Reverse ETL pipelines, a comprehensive data discovery process was performed to understand the structure, quality, and relationships within the Hospital Management dataset.

The objective was to identify:

- Available tables
- Primary and foreign keys
- Data quality issues
- Master and transaction tables
- Entity relationships
- Potential business use cases

---

# Dataset Summary

| Metric | Value |
|---------|------:|
| Domain | Healthcare |
| Total Tables | 18 |
| Largest Table | billing_detail (112,402 rows) |
| Smallest Table | diagnostic_test (9 rows) |
| Duplicate Records | 0 |
| Missing Values | Present only in `billing_detail.reference_id` |

---

# Tables Overview

| Table | Rows | Type |
|-------|-----:|------|
| patient | 30,000 | Master |
| admission | 45,000 | Transaction |
| billing | 45,000 | Transaction |
| billing_detail | 112,402 | Transaction |
| department | 11 | Master |
| doctor | 98 | Master |
| disease | 20 | Master |
| diagnostic_test | 9 | Master |
| drug | 250 | Master |
| drug_inventory | 250 | Master |
| drug_manufacturer | 300 | Master |
| employee | 500 | Master |
| insurance_provider | 50 | Master |
| patient_insurance | 21,617 | Transaction |
| patient_diagnostic | 63,269 | Transaction |
| prescription | 73,109 | Transaction |
| ward | 27 | Master |
| bed | 415 | Master |
| staff_assignment | 207 | Transaction |

---

# Master Tables

Master tables contain relatively static reference data.

- Patient
- Department
- Doctor
- Disease
- Drug
- Drug Inventory
- Drug Manufacturer
- Employee
- Insurance Provider
- Ward
- Bed
- Diagnostic Test

---

# Transaction Tables

Transaction tables store day-to-day hospital operations.

- Admission
- Billing
- Billing Detail
- Patient Insurance
- Patient Diagnostic
- Prescription
- Staff Assignment

---

# Data Quality Assessment

## Duplicate Records

No duplicate records were found across all tables.

**Status:** ✅ Passed

---

## Missing Values

Only one significant missing value was identified.

| Table | Column | Missing |
|--------|---------|---------:|
| billing_detail | reference_id | 67,402 |

### Observation

The `reference_id` column is nullable because certain billing charges (e.g., room charges or registration fees) may not reference another entity.

This appears to be a valid business rule rather than a data quality issue.

---

## Data Types

Observed data types include:

- Integer
- Float
- String
- Date (stored as Object)

Date columns were later converted into proper datetime format during ETL.

---

# Entity Relationships

## Core Business Flow

```text
Patient
    │
    ▼
Admission
    │
    ├─────────────► Billing
    │
    ├─────────────► Prescription
    │
    ├─────────────► Patient Diagnostic
    │
    ├─────────────► Disease
    │
    ├─────────────► Department
    │
    ├─────────────► Ward
    │
    └─────────────► Bed
```

---

# Relationship Mapping

| Parent Table | Child Table | Key |
|--------------|-------------|-----|
| Patient | Admission | patient_id |
| Admission | Billing | admission_id |
| Admission | Prescription | admission_id |
| Admission | Patient Diagnostic | admission_id |
| Admission | Disease | disease_id |
| Admission | Department | department_id |
| Admission | Ward | ward_id |
| Admission | Bed | bed_id |
| Department | Employee | department_id |
| Ward | Bed | ward_id |
| Drug | Drug Inventory | drug_id |
| Drug | Prescription | drug_id |
| Insurance Provider | Patient Insurance | insurance_provider_id |
| Patient | Patient Insurance | patient_id |

---

# Data Model

```text
Patient
   │
   ├───────────────┐
   ▼               ▼
Admission      Patient Insurance
   │
   ├──────────── Billing
   │
   ├──────────── Prescription
   │
   ├──────────── Patient Diagnostic
   │
   ├──────────── Disease
   │
   ├──────────── Department
   │                  │
   │                  ▼
   │              Employee
   │
   ├──────────── Ward
   │                  │
   │                  ▼
   │                 Bed
   │
   └──────────── Doctor
```

---

# Key Business Entities

### Patient

Stores demographic details of hospital patients.

### Admission

Represents each hospital visit.

### Billing

Captures financial transactions related to admissions.

### Department

Represents hospital departments such as Cardiology and Neurology.

### Disease

Stores diagnosis information.

### Prescription

Stores medicines prescribed during admission.

### Patient Diagnostic

Stores laboratory and diagnostic test records.

---

# Business Questions This Dataset Can Answer

- Which department generates the highest revenue?
- Which diseases have the highest admission rates?
- What is the average billing amount per department?
- Which patients have pending payments?
- Which wards have the highest occupancy?
- What is the average hospital stay by disease?
- Which insurance providers cover the highest claim amounts?
- Which drugs are prescribed most frequently?

---

# Conclusion

The Hospital Management dataset is highly normalized and suitable for demonstrating enterprise ETL, ELT, Reverse ETL, SQL, Data Warehousing, Data Modeling, Dashboarding, and Analytics Engineering workflows.

The dataset required minimal cleaning, making it ideal for focusing on data engineering concepts rather than data correction.