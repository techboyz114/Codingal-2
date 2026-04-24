a=int(input("Enter the first number : ")) #10
b=int(input("Enter the second number : ")) #99

for n in range(a,b+1): #a to b
    c=0 #count of factors
    for i in range(1,n+1): #1 to n
        if n%i==0:
            c+=1
    if c==2:
        print(n,'is prime number')
    else:
        print(n,'is not a prime number')

'''
n=8
c=0
i
1 -> 8%1=0 , c=1
2 -> 8%2=0 , c=2
3
4 -> 8%4=0 , c=3
5
6
7
8 -> 8%8=0 , c=4
'''