'''
Try the following questions on file handling:
1) write names of your friends in one file with gender in bracket i. e. Alina(F).
   Seperate your friends as per gender into two different files.
2) display the words in reverse order for each line
3) count palindrome words in the file like, dad
4) count special words in the file. (Starting and ending with same letter)
5) replace is with are and was with were in the file
6) merge two file content
'''

#2) display the words in reverse order for each line
fo = open("f1.txt")   # open file in read mode
L = fo.readline()
while L:
    words = L.strip().split()       # split line into words
    reversed_words = words[::-1]    # reverse the list of words
    print(" ".join(reversed_words)) # join back into a string
    L = fo.readline()
fo.close()
#3) count palindrome words in the file
fo = open("f1.txt")
L = fo.readline()
count = 0
while L:
    words = L.strip().split()
    for w in words:
        if w.lower() == w[::-1].lower():   # check palindrome ignoring case
            count += 1
    L = fo.readline()
fo.close()
print("Total palindrome words:", count)
#4) count special words in the file (starting and ending with same letter)
fo = open("f1.txt")
L = fo.readline()
count = 0
while L:
    words = L.strip().split()
    for w in words:
        if len(w) > 1 and w[0].lower() == w[-1].lower():  # first == last letter
            count += 1
    L = fo.readline()   
fo.close()
print("Total special words:", count)