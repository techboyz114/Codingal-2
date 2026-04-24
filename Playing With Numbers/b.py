#HCF
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
a=n1
b=n2
while n2!=0:
    n3=n2
    n2=n1%n2
    n1=n3
    HCF=n1
print("HCF of",a,"and",b,"is",HCF)