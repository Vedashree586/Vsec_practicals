
import pandas as pd
import numpy as np

# Create a DataFrame
data = {
    "Name": ["Amit", "Riya", "Rahul", "Sneha", "Priya"],
    "Department": ["CE", "IT", "CE", "IT", "CE"],
    "Marks": [85, np.nan, 78, 92, np.nan],
    "Age": [20, 21, 19, 22, 20]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 1. Handle Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print("\nAfter Filling Missing Values:")
print(df)

# 2. Replace Data
df["Department"] = df["Department"].replace("CE", "Computer")
print("\nAfter Replacing Data:")
print(df)

# 3. Filter Rows
print("\nStudents with Marks Greater than 85:")
print(df[df["Marks"] > 85])

# 4. Select Columns
print("\nSelected Columns:")
print(df[["Name", "Marks"]])

# 5. Sort Values
print("\nSorted by Marks:")
print(df.sort_values(by="Marks", ascending=False))

# 6. Group Values
print("\nAverage Marks by Department:")
print(df.groupby("Department")["Marks"].mean())

# 7. Group and Count Students
print("\nNumber of Students in Each Department:")
print(df.groupby("Department")["Name"].count())
