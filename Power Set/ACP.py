# Program to find all substrings of a string

def all_substrings(s):
    length = len(s)
    substrings = []
    for i in range(length):
        for j in range(i+1, length+1):
            substrings.append(s[i:j])
    return substrings

# Input from user
string = input("Enter a string: ")

# Get all substrings
result = all_substrings(string)

# Print substrings
print("All substrings are:")
for sub in result:
    print(sub)
