
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a sample dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 40, 50, 55, 65, 70, 80, 90],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95],
    "Department": ["CE", "IT", "CE", "IT",
                   "CE", "IT", "CE", "IT"]
}

df = pd.DataFrame(data)

# Set plot style
sns.set_style("whitegrid")

# 1. Line Plot
plt.figure()
sns.lineplot(data=df, x="Study_Hours", y="Marks",
             marker="o")
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# 2. Bar Plot
plt.figure()
sns.barplot(data=df, x="Department", y="Marks")
plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.show()

# 3. Histogram
plt.figure()
sns.histplot(data=df, x="Marks", bins=5, kde=True)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 4. Box Plot
plt.figure()
sns.boxplot(data=df, x="Department", y="Marks")
plt.title("Marks Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Marks")
plt.show()

# 5. Scatter Plot
plt.figure()
sns.scatterplot(data=df, x="Study_Hours", y="Marks",
                hue="Department", s=100)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()
