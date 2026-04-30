def is_power_of_8(n):
    if n <= 0:
        return False

    # check if n is power of 2 (only one set bit)
    if (n & (n - 1)) != 0:
        return False

    # count right shifts until n becomes 1
    shifts = 0
    while n > 1:
        n = n >> 1
        shifts += 1

    # power of 8 -> shifts must be multiple of 3
    return shifts % 3 == 0


num = int(input("Enter a number: "))
if is_power_of_8(num):
    print(num, "is a power of 8")
else:
    print(num, "is not a power of 8")
