def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

num = 29
print("Number of set bits:", count_set_bits(num))
