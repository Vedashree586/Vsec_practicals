
import matplotlib.pyplot as plt

# Sample Data
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [5, 15, 10, 20, 25]

# Create multiple subplots
fig, ax = plt.subplots(2, 2, figsize=(10, 8))

# 1. Line Plot
ax[0, 0].plot(x, y1, color='blue', marker='o',
              linestyle='-', label='Student A')
ax[0, 0].plot(x, y2, color='red', marker='s',
              linestyle='--', label='Student B')
ax[0, 0].set_title("Line Plot")
ax[0, 0].set_xlabel("Weeks")
ax[0, 0].set_ylabel("Marks")
ax[0, 0].legend()
ax[0, 0].grid(True)

# 2. Bar Plot
ax[0, 1].bar(x, y1, color='green', label='Marks')
ax[0, 1].set_title("Bar Plot")
ax[0, 1].set_xlabel("Weeks")
ax[0, 1].set_ylabel("Marks")
ax[0, 1].legend()
ax[0, 1].grid(axis='y', linestyle='--')

# 3. Scatter Plot
ax[1, 0].scatter(x, y2, color='purple',
                  marker='o', label='Student B')
ax[1, 0].set_title("Scatter Plot")
ax[1, 0].set_xlabel("Weeks")
ax[1, 0].set_ylabel("Marks")
ax[1, 0].legend()
ax[1, 0].grid(True)

# 4. Histogram
marks = [45, 55, 60, 65, 70, 70, 75, 80, 85, 90]
ax[1, 1].hist(marks, bins=5, color='orange',
              edgecolor='black', label='Marks')
ax[1, 1].set_title("Histogram")
ax[1, 1].set_xlabel("Marks")
ax[1, 1].set_ylabel("Frequency")
ax[1, 1].legend()
ax[1, 1].grid(axis='y', linestyle=':')

# Main title and layout
fig.suptitle("Student Performance Analysis", fontsize=16)
plt.tight_layout()
plt.show()
