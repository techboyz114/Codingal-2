#prime and palindrome
a=int(input("Enter a : "))
for n in range(1,a+1):
    c=0
    rev=0
    temp=n
    for i in range(1,temp+1):
        if temp%i==0:
            c+=1
    if c==2:
        while temp!=0: #353
            digit=temp%10 #3,5,3
            rev=rev*10+digit #0*10+3= 3*10 + 5=35*10+3=353
            temp=temp//10 #35,3,0
        if rev==n:
            print("Prime and palindrome",n)
        else:
            print(n,"is prime but not palindrome")
    else:
        print(n,"is not prime number")
