# Example DAX Measures

Total Revenue = SUM(Sales[Revenue])

Monthly Revenue =
CALCULATE([Total Revenue], DATESMTD('Date'[Date]))

Average Order Value = DIVIDE([Total Revenue], DISTINCTCOUNT(Sales[OrderID]))
