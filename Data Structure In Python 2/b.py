s1 = {6, 9, 1, 6, 2, 0, 2}#set : collection of unique elements : unordered collection of unique elementsprint('s1 : ', s1) #s1 and s2 are sets : collectionof unique elements : unordered collection of unique elements
s1.add(40)#add ele to set
print('s1 : ', s1)

s2 = {2, 4, 0}#set : collection of unique elements : unordered collection of unique elements
print('s2 : ', s2) #s1 and s2 are sets : collection of unique elements : unordered collection of unique elements

print(s1.difference(s2)) # s1 - s2 , common ele are removed from s1 and the remaining ele are returned
print(s1.symmetric_difference(s2)) # combine ele of s1 and s2 and then remove common ele from the combined set
print(s1.union(s2)) # all ele will be taken from both the sets
print(s1.intersection(s2)) # only common elements will be taken from both the sets