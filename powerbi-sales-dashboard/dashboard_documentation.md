# Power BI Dashboard Documentation

This document explains the layout and data model used in the Power BI sales dashboard.

Pages:
- Overview: KPIs (Revenue, Orders, AOV)
- Trends: Time series charts (monthly revenue, YoY growth)
- Products: Top products, product category performance
- Regions: Map and region performance

Data model:
- Fact table: Sales (OrderID, Date, ProductKey, CustomerKey, Quantity, Revenue)
- Dimension tables: Date, Product, Customer, Region

Tips:
- Use star schema for performance.
- Pre-aggregate in SQL for very large datasets.