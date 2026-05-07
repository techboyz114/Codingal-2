#flipping bits
def f1(n1,n2):
    flips=0
    while n1>0 or n2>0:
        t1=n1 & 1
        t2=n2 & 1
        if t1 !=t2:
            flips += 1
        n1 >>= 1
        n2 >>= 1
    return flips
x=int(input("Enter first number : "))
y=int(input("Enter second number : "))
print("Number of bits to be flipped : ",f1(x,y))