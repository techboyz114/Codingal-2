def f1(n):
    if n <= 0:
        return 0

    # check if n is power of 2 (only one set bit)
    if (n & (n - 1)) != 0:
        return 0

    # count right shifts
    c = 0
    while n > 1:
        n = n >> 1
        c += 1

    # power of 4 -> even number of shifts
    if c % 2 == 0:
        return 1
    else:
        return 0


num = int(input("Enter a number : "))
if f1(num):
    print(num, "is a power of 4")
else:
    print(num, "is not power of 4")