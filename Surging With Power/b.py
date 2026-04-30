#check if a number is power of 2
def f1(n):#32
    if n==0:
        return 0
    if (n&(n-1))==0:
        return 1
    return 0

n=int(input("Enter a number : "))
if f1(n):#32
    print(n,"is power of 2")
else:
    print(n,"is not power of 2")

'''
n=8
8= 1000
&
7= 0111
    0000
'''
