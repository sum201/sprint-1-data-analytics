import pandas as pd

# Load data
sales_data = pd.read_csv('sales_data.csv')

# Check for missing values
print(sales_data.isnull().sum())

# Fill missing values or drop rows with missing data
sales_data.fillna(method='ffill', inplace=True)

# Convert date columns to datetime format
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'])

# Remove duplicates
sales_data.drop_duplicates(inplace=True)

# Save cleaned data
sales_data.to_csv('cleaned_sales_data.csv', index=False)


import matplotlib.pyplot as plt
import seaborn as sns

# Sales trend over time
sales_data.groupby(sales_data['Order Date'].dt.to_period("M"))['Sales'].sum().plot(kind='line')
plt.title('Sales Over Time')
plt.show()

# Top-selling products
top_products = sales_data.groupby('Product')['Sales'].sum().sort_values(ascending=False)
sns.barplot(x=top_products.index, y=top_products.values)
plt.xticks(rotation=90)
plt.title('Top-Selling Products')
plt.show()
