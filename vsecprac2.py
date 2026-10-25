
import numpy as np

# 1. Create a 1D array using np.array()
a = np.array([10, 20, 30, 40, 50])
print("1D Array:", a)

# 2. Create an array using np.arange()
b = np.arange(1, 11)
print("\nArray using arange:", b)

# 3. Create an array using np.linspace()
c = np.linspace(0, 10, 5)
print("Array using linspace:", c)

# 4. Indexing
print("\nIndexing")
print("First element:", a[0])
print("Third element:", a[2])

# 5. Slicing
print("\nSlicing")
print("First three elements:", a[0:3])
print("Last two elements:", a[3:5])

# 6. Create a 2D array
d = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("\n2D Array:\n", d)

# 7. Indexing in 2D array
print("\n2D Indexing")
print("Element at row 1, column 2:", d[0, 1])
print("Element at row 2, column 3:", d[1, 2])

# 8. Slicing in 2D array
print("\n2D Slicing")
print("First two rows:\n", d[0:2, :])
print("First two columns:\n", d[:, 0:2])

# 9. Reshaping
e = np.arange(1, 7)
f = np.reshape(e, (2, 3))
print("\nOriginal Array:", e)
print("Reshaped 2D Array:\n", f)

# 10. Mathematical functions
print("\nMathematical Functions")
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))

# Mathematical functions on 2D array
print("\nSum of 2D Array:", np.sum(d))
print("Mean of 2D Array:", np.mean(d))
print("Sum of each column:", np.sum(d, axis=0))
print("Sum of each row:", np.sum(d, axis=1))
