'''
file handling:

1) open the file
2) modes of operation :
   a) read:
      -> r
      -> file must be existing otherwise it will give us an error
      -> default mode

   b) write
      -> w
      -> if the file is not existing then new file will be created automatically
      -> if the file is already existing then the earlier content of file will be overwritten with new content

   c) append
      -> a
      -> if the file is not existing then new file will be created automatically
      -> if the file is already existing then the new content will be added at the end of earlier content
'''
      
#1) Read the full file
fo=open("f1.txt") #read mode
print(fo.read()) #reading complete file
fo.close()

#2) read first five characters only
fo=open("f1.txt") #read mode
print(fo.read(5))
print(fo.read(5))
fo.close()

#3) count vowels in the file
fo=open("f1.txt")
ch=fo.read(1)
c=0
while ch: #if ch is existing
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        c+=1
    ch=fo.read(1)
print("Total number of vowels : ",c)

#4) count number of lines
fo=open("f1.txt")
ch=fo.read(1)
