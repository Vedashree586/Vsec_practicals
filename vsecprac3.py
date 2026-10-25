
import numpy as np

# 1. Create NumPy arrays
a = np.array([1, 4, 9, 16])
b = np.array([10, 20, 30, 40])

print("Array A:", a)
print("Array B:", b)

# 2. Vectorized Operations
print("\nVectorized Operations")
print("Addition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)

# 3. Universal Functions (ufuncs)
print("\nUniversal Functions")
print("Using np.add():", np.add(a, b))
print("Using np.sqrt():", np.sqrt(a))
print("Using np.exp():", np.exp(a))

# 4. Broadcasting with a Scalar
c = np.array([10, 20, 30])
print("\nBroadcasting with Scalar")
print("Array:", c)
print("Array + 5:", c + 5)

# 5. Broadcasting with Two Arrays
x = np.array([[1], [2], [3]])
y = np.array([10, 20, 30])

print("\nBroadcasting with Two Arrays")
print("Array X:\n", x)
print("Array Y:", y)
print("Result:\n", x + y)

# 6. Broadcasting Rules Example
p = np.array([[1, 2, 3],
              [4, 5, 6]])
q = np.array([10, 20, 30])

print("\nBroadcasting Rules")
print("Array P:\n", p)
print("Array Q:", q)
print("P + Q:\n", p + q)
