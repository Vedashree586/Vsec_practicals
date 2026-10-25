
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create monthly sales and advertising dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Sales": [12000, 15000, 13500, 18000, 22000, 20000,
              25000, 23000, 28000, 30000, 27000, 35000],
    "Advertising": [3000, 3500, 3200, 4000, 4500, 4200,
                    5000, 4800, 5500, 6000, 5700, 7000]
}

df = pd.DataFrame(data)

# Customer visits dataset
visits = [2, 3, 4, 5, 3, 6, 4, 2, 7, 5,
          3, 4, 8, 6, 5, 3, 4, 9, 2, 5]

# Display dataset
print("Monthly Sales and Advertising Dataset:")
print(df)

# Summary statistics
print("\nSummary Statistics:")
print(df[["Sales", "Advertising"]].describe())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 1. Line plot of monthly sales
plt.figure(figsize=(8, 5))
sns.lineplot(data=df, x="Month", y="Sales", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (Rs.)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar plot of monthly advertising spend
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Month", y="Advertising")
plt.title("Monthly Advertising Spend")
plt.xlabel("Month")
plt.ylabel("Advertising Spend (Rs.)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Distribution of customer visits
plt.figure(figsize=(8, 5))
sns.histplot(visits, bins=6, kde=True)
plt.title("Distribution of Customer Visits")
plt.xlabel("Number of Visits")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4. Sales distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Sales", bins=6, kde=True)
plt.title("Sales Distribution")
plt.xlabel("Monthly Sales (Rs.)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
