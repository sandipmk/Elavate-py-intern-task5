# Data Analysis on csv file...
#----------------------------
import pandas as pd
import matplotlib.pyplot as plt

# ====================
# Load & Prepare Data
# ====================
df = pd.read_csv(r'd:\Elevate lab py inetrn\sample_data.csv')

# Revenue column add
df['Revenue'] = df['Quantity'] * df['Price']

# Date ko datetime me convert
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'])

# ==============
# data Analysis
# ==============
# Total Revenue per City
city_revenue = df.groupby('City')['Revenue'].sum().sort_values(ascending=False)

# Total Revenue per Product
product_revenue = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

# Total Quantity per Product
product_quantity = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)

# Revenue Over Time (Daily)
revenue_over_time = df.groupby('Purchase_Date')['Revenue'].sum().sort_index()

# ===============
# Print Insights
# ===============
print("\n--- Data Analysis Insights ---")
print("\nTotal Revenue per City:\n", city_revenue)
print("\nTotal Revenue per Product:\n", product_revenue)
print("\nTotal Quantity per Product:\n", product_quantity)

# =======================
# Visualization Function
# =======================
def plot_bar(data, title, xlabel, ylabel, color, save_path, show_values=True):
    plt.figure(figsize=(12, 6))
    bars = data.plot(kind='bar', color=color, edgecolor='black')
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right')

    # Bar values on top
    if show_values:
        for p in bars.patches:
            bars.annotate(f'{p.get_height():,.0f}',
                          (p.get_x() + p.get_width() / 2., p.get_height()),
                          ha='center', va='bottom', fontsize=10, color='black')

    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()

# ==============
# Create Charts
# ==============
plot_bar(city_revenue,
         'Total Revenue by City',
         'City', 'Revenue ($)',
         'skyblue',
         r'd:\Elevate lab py inetrn\revenue_by_city.png')

plot_bar(product_revenue,
         'Total Revenue by Product',
         'Product', 'Revenue ($)',
         'lightgreen',
         r'd:\Elevate lab py inetrn\revenue_by_product.png')

plot_bar(product_quantity,
         'Total Quantity by Product',
         'Product', 'Quantity Sold',
         'orange',
         r'd:\Elevate lab py inetrn\quantity_by_product.png')

# ============================
# STEP 6: Revenue Over Time (Line Chart)
# ============================
plt.figure(figsize=(12, 6))
plt.plot(revenue_over_time.index, revenue_over_time.values, marker='o', linestyle='-', color='purple')
plt.title('Revenue Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(r'd:\Elevate lab py inetrn\revenue_over_time.png')
plt.show()

print("\n--- Charts Generated Successfully ---")
print("1. revenue_by_city.png")
print("2. revenue_by_product.png")
print("3. quantity_by_product.png")
print("4. revenue_over_time.png")
