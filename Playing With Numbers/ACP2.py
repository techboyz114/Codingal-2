#Count The Number Of Zeros in a number
n=int(input("Enter a number : "))
count=0
while n!=0:
    d=n%10
    if d==0:
        count+=1
    n=n//10
print("Number of zeros in the given number is :",count)
#themku guys bye bye see u tommorrow