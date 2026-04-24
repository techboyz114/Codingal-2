def factor(n):#n=14
    print("Factors of",n,"are : ")
    for i in range(1,n+1):#i: 1 to 14
        if n%i==0:#14%1 =0, 14%2=0,14%3=2..........14%14=0
            print(i)
x=int(input("Enter your number : "))
factor(x)#14

'''
14:
1: 14%1=0
2: 14%2=0
7: 14%7=0
14:14%14=0

if remainder is 0 then it is factor

14%3=2  remainder is not 0, so 3 is not factor

'''