#tuple
#empty tuple
T=()
print(T)
T=tuple()
print(T)

#single ele
T=(30) #not a tuple but it is a number
print(T, type(T))
T=(30,)
print(T, type(T))

#Tuple with many ele
T=(6,1,8,1,2,9,10) #Tuple : immutable : non changable
L=[6,1,8,1,2,9,10] #List : mutable : changable
L[2]=100
print(L)
#T[2]=100

T=(6,1,8,1,2,9,10)
print(sum(T))
print(max(T))
print(min(T))

t=(5,7,4)
a, b, c = t
print(b)

T = a, b, c
print(T)

# create list from tuple
# method 1
L = list(T)

# method 2
L = []
for x in T:
    L.append(x)

T = (3, 30, 7, 2, 4, 6, 9, 90, 1, 60)
print(T[3])
print(T[-3])
print(T[2:7])  # 7, 2, 4, 6, 9

T = (3, 30, 7, (2, 4, (6, 9), 90, 1), 60)
print(T[3][1])  # 4
print(T[3][2][1])  # 9
