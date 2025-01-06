import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
data = pd.read_csv('data/sales_data.csv', parse_dates=['date'])

# Add a 'month' column for grouping
data['month'] = data['date'].dt.to_period('M')

# Calculate monthly sales summary
monthly_sales = data.groupby('month')['sales_amount'].sum()

# Plot Sales Trend
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales Amount', fontsize=14)
plt.grid(True)

# Add labels to each data point
for i, (month, sales) in enumerate(monthly_sales.items()):
    plt.text(i, sales, f'{sales:.0f}', fontsize=10, ha='center', va='bottom')

# Save the plot
plt.savefig('data/sales_trend.png')
plt.show()

# Display top products by sales
top_products = data.groupby('product_name')['sales_amount'].sum().sort_values(ascending=False)
print("Top Products by Sales:")
print(top_products)

# Save summarized monthly sales to a CSV
monthly_sales.to_csv('data/monthly_sales_summary.csv', header=['sales_amount'])
print("Monthly sales summary saved to 'data/monthly_sales_summary.csv'")

