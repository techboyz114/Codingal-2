# number of zeros and ones
def f1(n):  # 1001
    c = 1
    while (n):
        if n & 1 == 1:
            position = c
            break
        c += 1
        n = n >> 1
    print("First set bit is at position :", position)

num = int(input("Enter a number : "))
f1(num)