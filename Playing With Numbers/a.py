#palindrome

n=int(input("Enter a number : ")) #1221
#reverse number
m=n #1221
Rev=0
while n!=0:
    d=n%10
    Rev=Rev*10+d
    n=n//10
    #Last digit : 1221//10=1, 1221%10 = 1, 12%10 = 2, 1%10 = 1
    # 0*10+1=1, 1*10+2= 12, 12*10 + 2= 122, 122*10+1=1221
    #1221//10= 122 , 122//10 = 12, 12//10=1, 1//10=0

if Rev==m:
    print(m,"is palindrome number")
else:
    print(m,"is not palindrome number")
