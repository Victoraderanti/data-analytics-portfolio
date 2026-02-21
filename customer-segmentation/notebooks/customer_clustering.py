import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load sample customer data
# df = pd.read_csv('../data/sample_customers.csv')

# Example placeholder dataframe
df = pd.DataFrame({
    'Age': [25, 45, 33, 52, 23, 37],
    'AnnualIncome': [35000, 82000, 54000, 120000, 28000, 64000],
    'SpendingScore': [60, 40, 50, 20, 73, 45]
})

# Preprocess
scaler = StandardScaler()
X = scaler.fit_transform(df)

# Fit KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)

df['Segment'] = labels
print(df.groupby('Segment').mean())

# Simple visualization
plt.scatter(df['AnnualIncome'], df['SpendingScore'], c=labels, cmap='tab10')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.title('Customer Segments')
plt.show()