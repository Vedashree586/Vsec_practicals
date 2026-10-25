
import numpy as np

# Create a matrix
A = np.array([[2, 1],
              [1, 3]])

print("Matrix A:")
print(A)

# 1. Solve matrix equations: AX = B
B = np.array([5, 6])
X = np.linalg.solve(A, B)

print("\nSolution of AX = B:")
print(X)

# 2. Find inverse of matrix
inverse = np.linalg.inv(A)
print("\nInverse of Matrix A:")
print(inverse)

# 3. Find transpose of matrix
transpose = A.T
print("\nTranspose of Matrix A:")
print(transpose)

# 4. Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)