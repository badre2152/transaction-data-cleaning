# financecore-transactions-analysis-

## Project Overview

This project focuses on cleaning, validating, and enriching a banking transactions dataset.
The goal is to transform raw transactional data into a high-quality, structured dataset ready for analysis, reporting, and database integration.

## Objectives

* Improve data quality (handle missing values, inconsistencies, duplicates)
* Detect anomalies using statistical methods (IQR)
* Build meaningful business indicators (KPIs)
* Prepare clean data for PostgreSQL and dashboard visualization

## Tech Stack

* Python (Pandas, NumPy)
* Jupyter Notebook
* Git & GitHub

## Project Structure

```
financecore-transactions-analysis/
├── data/
│   ├── brut/
│   └── processed/
├── docs/
│   └── decisions.md         
├── notebooks/
│   └── data_cleaning.ipynb  
└── requirements.txt         
```

## Key Features

* End-to-end data cleaning pipeline
* Outlier detection using IQR method
* Risk classification model
* Client-level KPIs computation
* Data standardization and validation

## Output

* Clean dataset: `financecore_clean.csv`
* Ready for database integration and dashboarding

## Author

* BRAHIM BADRE
