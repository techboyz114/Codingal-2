#bitwise operations
n1=17 #10001
n2=4  #00100

print(n1 , n2, bin(n1), bin(n2))
#and
print(n1 & n2, bin(n1 & n2)) #0
#or
print(n1 | n2, bin(n1 | n2)) #10101
#not
print(~n1, bin(~n1)) #01110
#XOR
print(n1 ^ n2, bin(n1 ^ n2)) #10101
#Right shift
print(n1 >> 1, bin(n1 >> 1)) #01000
#Left shift
print(n1 << 1, bin(n1 << 1)) #0010
