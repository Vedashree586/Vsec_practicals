
# Demonstration of Python Data Types and Operations

import math

# 1. Integer
a = 10
b = 3
print("Integer:", a)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Integer Division:", a // b)
print("Power:", a ** b)

# 2. Float
x = 12.5
print("\nFloat:", x)
print("Round:", round(x))
print("Absolute Value:", abs(-12.5))

# 3. Complex
c = 2 + 3j
print("\nComplex:", c)
print("Real Part:", c.real)
print("Imaginary Part:", c.imag)
print("Conjugate:", c.conjugate())

# 4. String
s = "Python Programming"
print("\nString:", s)
print("Length:", len(s))
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Replace:", s.replace("Python", "Java"))

# 5. List
lst = [10, 20, 30, 40]
print("\nList:", lst)
lst.append(50)
print("After Append:", lst)
lst.remove(20)
print("After Remove:", lst)
print("Length:", len(lst))
print("Maximum:", max(lst))
print("Minimum:", min(lst))

# 6. Tuple
t = (10, 20, 30, 20)
print("\nTuple:", t)
print("Length:", len(t))
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))

# 7. Dictionary
d = {"name": "Amit", "age": 20, "marks": 85}
print("\nDictionary:", d)
print("Name:", d["name"])
d["city"] = "Pune"
print("After Adding Item:", d)
print("Keys:", list(d.keys()))
print("Values:", list(d.values()))
print("Items:", list(d.items()))

# 8. Set
st = {10, 20, 30, 40}
st.add(50)
print("\nSet:", st)
st.discard(20)
print("After Removing 20:", st)
print("Union:", st | {40, 60})
print("Intersection:", st & {30, 40, 50})

# 9. Frozenset
fs = frozenset([1, 2, 3, 4])
print("\nFrozenset:", fs)
print("Length:", len(fs))
print("Contains 2:", 2 in fs)
print("Union:", fs | frozenset([4, 5, 6]))

# 10. Boolean
p = True
q = False
print("\nBoolean:", p, q)
print("AND:", p and q)
print("OR:", p or q)
print("NOT:", not p)

# 11. None Type
n = None
print("\nNone Type:", n)
print("Is None:", n is None)
print("Type:", type(n))

# 12. Built-in Functions
numbers = [5, 10, 15, 20]
print("\nBuilt-in Functions")
print("Type:", type(numbers))
print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sorted:", sorted(numbers))

# 13. Mathematical Functions
print("\nMathematical Functions")
print("Square Root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Factorial:", math.factorial(5))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))
print("GCD:", math.gcd(12, 18))
print("Value of Pi:", math.pi)
