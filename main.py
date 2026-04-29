import pandas as pd
df = pd.read_csv("data.csv")
print(df)
df["Total"] = df["Quantity"] * df["Price"]
print(df)
print("Total Sales:", df["Total"].sum())
print(df.groupby("Product")["Total"].sum())
print("\nSales by Product:")
print(df.groupby("Product")["Total"].sum())
import matplotlib.pyplot as plt
sales_by_product = df.groupby("Product")["Total"].sum()
sales_by_product.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.savefig("chart.png")
plt.close()
print("Chart saved as chart.png")