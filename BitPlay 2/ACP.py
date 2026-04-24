def f1(n):
    result = 0
    while n > 0:
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

# Example usage
num = 13   # Binary: 1101
reversed_num = f1(num)  # 1011
print("Original:", bin(num))
print("Reversed:", bin(reversed_num))