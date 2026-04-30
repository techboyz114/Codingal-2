#program to find x^y
x=int(input("Enter x : "))
y=int(input("Enter y : "))
res=1
while y>0:
    if y%2==0:
        x=x*x
        y=y>>1
    else:
        res=res*x
        y=y-1
print("x^y =",res)

...
2^4
...
