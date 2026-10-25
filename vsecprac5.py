
import pandas as pd

# 1. Create a Series
s = pd.Series([10, 20, 30, 40, 50])
print("Pandas Series:")
print(s)

# 2. Create a DataFrame
data = {
    "Name": ["Amit", "Riya", "Rahul", "Sneha"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 95]
}

df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# 3. Display basic information
print("\nFirst two rows:")
print(df.head(2))

print("\nDataFrame Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# 4. Select a column
print("\nNames:")
print(df["Name"])

# 5. Select a row
print("\nFirst row:")
print(df.iloc[0])

# 6. Add a new column
df["Result"] = ["Pass", "Pass", "Pass", "Pass"]
print("\nAfter adding a column:")
print(df)

# 7. Filter data
print("\nStudents scoring above 80:")
print(df[df["Marks"] > 80])

# 8. Sort data
print("\nSorted by Marks:")
print(df.sort_values("Marks"))

# 9. Export DataFrame to CSV
df.to_csv("students.csv", index=False)
print("\nData exported to students.csv")

# 10. Import CSV file
df2 = pd.read_csv("students.csv")
print("\nData imported from CSV:")
print(df2)

# 11. Basic operations
print("\nTotal Marks:", df2["Marks"].sum())
print("Average Marks:", df2["Marks"].mean())
print("Highest Marks:", df2["Marks"].max())
print("Lowest Marks:", df2["Marks"].min())
print("Number of Students:", len(df2))
