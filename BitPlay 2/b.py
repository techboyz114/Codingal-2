# One odd occurring number in an array
n = int(input("How many elements in the array? "))  # Example: 7
ar = []
i = 1
while i <= n:  # Fill array
    x = int(input("Enter a number: "))
    ar.append(x)
    i += 1

res = 0
for x in ar:  # XOR all elements
    res = res ^ x

print(res, "is the odd occurring number in array", ar)
