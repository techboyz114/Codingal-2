#HCF and LCM
n1 = int(input("Enter first number: "))   # Example: 12
n2 = int(input("Enter second number: "))  # Example: 18

a = n1
b = n2

while b != 0:
    temp = b
    b = a % b
    a = temp

HCF = a
LCM = (n1 * n2) // HCF

print("HCF =", HCF)
print("LCM =", LCM)
