# DECISIONS.md – Data Cleaning & Preparation

## Project: FinanceCore SA – Bank Transactions Audit

## Date: 2026

## Author: BRAHIM BADRE

---

# 1. Data Exploration Decisions

### ✔ Observations

* Dataset contains **2060 rows and 16 columns**
* Presence of:

* Missing values in critical fields (score_credit_client, segment_client, agence)
* Duplicate transaction IDs
* Inconsistent date formats
* Incorrect numeric formats (comma instead of dot)
* Outliers in transaction amounts and credit scores
* Inconsistent text formatting (case, spaces)

### ✔ Decision

A full data cleaning pipeline was required before any analysis or modeling.

---

# 2. Duplicate Handling

### ✔ Issue

* Duplicate `transaction_id` detected with slight differences in timestamps

### ✔ Decision

* Kept the **first occurrence** based on chronological order
* Assumption: earliest record is Most Reliable

```python
df = df.sort_values(by='date_transaction')
df = df.drop_duplicates(subset='transaction_id', keep='first')
```

---

# 3. Date Format Standardization

### ✔ Issue

* Mixed formats: `DD/MM/YYYY` and `YYYY-MM-DD`

### ✔ Decision

* Converted all values to `datetime` format using pandas
* Invalid dates were coerced to NaT

```python
df['date_transaction'] = pd.to_datetime(df['date_transaction'], errors='coerce', dayfirst=True)
```

---

# 4. Monetary Values Cleaning

### ✔ Issue

* Use of commas instead of dots (e.g., "123,45")
* Non-numeric formatting

### ✔ Decision

* Replaced commas with dots and converted to float

```python
df['montant'] = df['montant'].astype(str).str.replace(',', '.', regex=False).astype(float)
```

---

# 5. Account Balance Cleaning (solde_avant)

### ✔ Issue

* Values include text suffix "EUR"

### ✔ Decision

* Removed text and converted to numeric

```python
df['solde_avant'] = df['solde_avant'].astype(str).str.replace(' EUR', '', regex=False).astype(float)
```

---

# 6. Categorical Data Standardization

### ✔ Issues

* Lowercase currencies (eur)
* Inconsistent casing in segment_client
* Extra spaces in agence

### ✔ Decisions

* Converted currencies to uppercase
* Standardized segment names (capitalize)
* Trimmed whitespace

```python
df['devise'] = df['devise'].str.upper().str.strip()
df['segment_client'] = df['segment_client'].str.capitalize().str.strip()
df['agence'] = df['agence'].str.strip()
```

---

# 7. Missing Values Treatment

### ✔ Issues

* Missing values in:

* score_credit_client (numeric)
* segment_client (categorical)
* agence (categorical)

### ✔ Decisions

* Numeric → imputed using **median**
* Categorical → imputed using **mode**

### ✔ Justification

* Median is robust to outliers
* Mode preserves most frequent category

```python
df['score_credit_client'] = df['score_credit_client'].fillna(df['score_credit_client'].median())
df['segment_client'] = df['segment_client'].fillna(df['segment_client'].mode()[0])
df['agence'] = df['agence'].fillna(df['agence'].mode()[0])
```

---

# 8. Outliers Detection

### ✔ Issues

* Extreme values in `montant`
* Invalid credit scores (<0 or >850)

### ✔ Decision

* Used **IQR method** to detect anomalies
* Did NOT remove outliers
* Created a flag column `is_anomaly`

### ✔ Justification

* Outliers may represent real fraud or rare events
* Important for risk analysis

```python
df['is_anomaly'] = (df['montant'] < lower) | (df['montant'] > upper)
```

---

# 9. Feature Engineering

### ✔ Created Features

* Time-based:

* annee, mois, trimestre, jour_semaine
* Financial:

* montant_eur_verifie
* Risk:

* categorie_risque
* Client metrics:

* solde_net
* nb_transactions
* montant_moyen
* nb_produits
* Operational:

* taux_rejet par agence

### ✔ Justification

* Improve analytical capabilities
* Enable dashboard insights for management

---

# 10. Data Quality Validation

### ✔ Checks Performed

* No critical missing values remaining
* Correct data types
* Consistency between calculated and original fields
* No duplicate transaction_id

---

# 11. Final Output

### ✔ Result

* Clean and enriched dataset: `financecore_clean.csv`

### ✔ Usage

* Ready for:

* PostgreSQL integration
* BI dashboards (Streamlit / Power BI)

---

# 12. Key Takeaways

* Data cleaning is critical before analysis
* Outliers should not always be removed
* Documentation ensures reproducibility
* Structured pipeline improves scalability

---
