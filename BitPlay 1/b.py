# nth bit in a number is set bit or not
def f1(num, n):  # 100110, 3 -> 100110 & 000100, 000
    if num & (1 << (n - 1)):
        print("\n Set")
    else:
        print("\n Not Set")

x = int(input("Enter a number : "))
n = int(input("Enter bit number to check : "))
f1(x, n)

'''
set bit = 1
n = 3
1001101 & 00000100
c = 1
while n & 1 == 1:
    n = n >> 1

c = c + 1
'''
