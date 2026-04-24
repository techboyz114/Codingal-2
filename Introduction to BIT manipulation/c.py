#number of bits
n=int(input("Enter n : "))
c=0
while n:
    c += 1
    n>>=1
print(c)

'''
0101
>>
0010
0001
0000
'''
