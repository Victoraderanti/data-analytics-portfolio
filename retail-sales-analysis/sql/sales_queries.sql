-- Total sales by product
SELECT Product, SUM(Revenue) AS TotalRevenue
FROM retail_sales
GROUP BY Product
ORDER BY TotalRevenue DESC
LIMIT 10;

-- Monthly sales trend
SELECT DATE_TRUNC('month', OrderDate) AS Month, SUM(Revenue) AS MonthlyRevenue
FROM retail_sales
GROUP BY Month
ORDER BY Month;