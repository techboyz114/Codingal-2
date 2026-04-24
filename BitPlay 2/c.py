# Two odd occurring numbers in an array
n = int(input("How many elements in the array? "))  # Example: 8
ar = []
i = 1
while i <= n:  # Fill array
    x = int(input("Enter a number: "))
    ar.append(x)
    i += 1

x2 = ar[0]
x = 0
y = 0
b = 0  # check set bit

# XOR all elements
for i in range(1, n):
    x2 = x2 ^ ar[i]

# Find rightmost set bit
b = x2 & ~(x2 - 1)

# Divide elements into two groups based on that bit
for i in range(n):
    if ar[i] & b:
        x = x ^ ar[i]
    else:
        y = y ^ ar[i]

print("The two odd occurring elements are:", x, "and", y)
