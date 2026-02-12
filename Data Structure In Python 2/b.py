s1 = {6, 9, 1, 6, 2, 0, 2}
s1.add(40)
print('s1 : ', s1)

s2 = {2, 4, 0}
print('s2 : ', s2)

print(s1.difference(s2)) # s1 - s2 , common ele are removed from s1
print(s1.symmetric_difference(s2)) # combine ele of s1 and s2 and then remove common ele
print(s1.union(s2)) # all ele will be taken from both the sets
print(s1.intersection(s2)) # only common elements