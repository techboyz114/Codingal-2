n=int(input("Enter a number: "))
m=n
if n==0:
    print(m, "is not power of 2")
else:
    while n%2==0:
        n=n//2
    if n==1:
        print(m, "is power of 2")
    else:
        print(m, "is not power of 2")
