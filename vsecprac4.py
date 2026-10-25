
import numpy as np

# 1. Generate random numbers using rand()
a = np.random.rand(5)
print("Random numbers between 0 and 1:", a)

# 2. Generate random numbers using randn()
b = np.random.randn(5)
print("\nNormally distributed standard random numbers:", b)

# 3. Generate random integers using randint()
c = np.random.randint(1, 100, 5)
print("\nRandom integers:", c)

# 4. Generate numbers using normal()
d = np.random.normal(50, 10, 5)
print("\nNormal distribution (mean=50, std=10):", d)

# 5. Simulate a uniform distribution
uniform = np.random.rand(1000)
print("\nUniform Distribution Statistics")
print("Mean:", np.mean(uniform))
print("Variance:", np.var(uniform))
print("Standard Deviation:", np.std(uniform))

# 6. Simulate a normal distribution
normal = np.random.normal(50, 10, 1000)
print("\nNormal Distribution Statistics")
print("Mean:", np.mean(normal))
print("Variance:", np.var(normal))
print("Standard Deviation:", np.std(normal))

# 7. Statistics of random integers
print("\nRandom Integer Statistics")
print("Sum:", np.sum(c))
print("Minimum:", np.min(c))
print("Maximum:", np.max(c))
print("Mean:", np.mean(c))
