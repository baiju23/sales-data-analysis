import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
data = {
    'Product': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Sales': [1000, 1500, 2000, 1200, 1700, 2200]
}

df = pd.DataFrame(data)

# Group by Product
sales = df.groupby('Product')['Sales'].sum()

print(sales)

# Plot
sales.plot(kind='bar')
plt.title('Sales Analysis')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.show()