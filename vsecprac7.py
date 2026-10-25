
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 1. Line Plot
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 2. Bar Plot
plt.figure()
plt.bar(x, y)
plt.title("Bar Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 3. Scatter Plot
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 4. Histogram
marks = [45, 55, 60, 65, 70, 70, 75, 80, 85, 90, 95, 60, 75, 80, 85]

plt.figure()
plt.hist(marks, bins=5, edgecolor='black')
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
