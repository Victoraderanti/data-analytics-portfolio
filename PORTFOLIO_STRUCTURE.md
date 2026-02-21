# Portfolio Structure Guide

This document describes the recommended folder and file structure for the data analytics portfolio repository.

Recommended layout:

```
data-analytics-portfolio/
├── README.md                       # Portfolio index and links to projects
├── PORTFOLIO_STRUCTURE.md          # This structure guide
├── INTERVIEW_GUIDE.md              # Tips for presenting projects in interviews
├── retail-sales-analysis/
│   ├── README.md
│   ├── notebooks/
│   │   └── 01_EDA.ipynb
│   ├── sql/
│   │   └── sales_queries.sql
│   └── data/
│       └── sample_retail_sales.csv
├── customer-segmentation/
│   ├── README.md
│   ├── notebooks/
│   │   └── customer_clustering.py
│   └── data/
│       └── sample_customers.csv
├── powerbi-sales-dashboard/
│   ├── README.md
│   ├── dashboard_documentation.md
│   └── dax_formulas.md
└── etl-automation-pipeline/
    ├── README.md
    ├── etl_script.py
    ├── requirements.txt
    └── config/
        └── example_config.yaml
```

Notes:
- Keep data small or provide links to datasets to keep the repo lightweight.
- Add screenshots to the `visualizations/` or `reports/` folder inside each project when available.
- Use descriptive commit messages and small incremental commits to show progress.

How to use this guide:
- Copy this structure as a template when adding new projects.
- Update README files with project-specific instructions and data sources.

---

Created by Victoraderanti.
