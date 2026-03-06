#1) read a line from file
fo=open("f1.txt")
L=fo.read() #read entire file content
print(L)
print('*'*10)
fo.seek(0)
L=fo.read(5) #read only 5 characters of file content
print(L)
print('*'*10)
fo.seek(0)
fo=open("f1.txt")
L=fo.readline() #read one complete line
print(L)
fo.close()
print('*'*10)

#2) read 3 lines
fo=open("f1.txt")
for i in range(3):
    L=fo.readline() #read a line with \n (enter key/ new line character)
    print(L,end="")

#read, write and append
#'r' : read(): 1 character
#readline()
#3) count and display all the lines of file  
fo=open("f1.txt") #read mode  
L=fo.readline()  #1st line  
#line is read with \n (new line char/enter key) at the end  
c=0  
while L: #line is existing  
    c=c+1 #1,2  
    print(L.strip()) #line has \n at the end + print  
    #print(L, end='')  
    L=fo.readline() #next line  
print(c)  

#4) display only odd lines  
fo=open("f1.txt")  
L=fo.readline()  
#line is read with \n (new line char/enter key) at the end  
c=0  
while L:  
    c=c+1 #1  
    if c%2!=0:  
        print(L.rstrip())  
    L=fo.readline()  

fr=open("f1.txt")#read mode
fw=open("f11.txt",'w')#write mode, if the file is not existing then will be created automatically
L=fr.readline()
#line is read with \n(new line char/enter key) at the end
c=0
while L:
    c=c+1
    if c%2!=0:
        fw.write(L)
    L=fr.readline()
fr.close()
fw.close()

#6) take only those lines which start with 't'
fr=open("f1.txt")#read mode
fw=open("f11.txt",'w')#write mode
L=fr.readline()
#line is read with \n(new line char/enter key) at the end
while L:
    if L.startswith('t'):
        fw.write(L)
    L=fr.readline()
fr.close()
fw.close()

#7) count the number of words in each line
fo=open("f1.txt") #file opened in read
L=fo.readline() #1st line
#line is read with \n (new line char/enter key) at the end
c=0
while L:
    c=c+1 #1,2
    Li=L.split() #[hello, how, are, you?]
    print("Line",c,"Total number of words = ",len(Li))
    L=fo.readline()

#8) count the number of words starting with 'T' or 't'
fo=open("f1.txt") #file opened in read
L=fo.readline() #1st line
#line is read with \n (new line char/enter key) at the end
c=0
while L:
    Li=L.split() #[hello, how, are, you?]
    for w in Li:
        if w[0]=='T' or w[0]=='t':
            c+=1
    L=fo.readline()
print(c)
#ACP
#8)display the longest word from each line
fo=open("f1.txt")
L=fo.readline()
#line is read with \n(new line char/enter key) at the end
while L:
    Li=L.split() #[ "Hello","Every",'Morning','Sunlight','from','east']
    x=0 #to store length of word
    for w in Li: #Hello,Every,Morning,Sunlight,from,east
        y=len(w) #y=5,5,7,8,4,4
        if y>x:
            x=y #x=5, 7 ,8
            w1=w #w1=hello, Morning, Sunlight
    print("longest word in",L,"is",w1,"with",x,"characters\n\n")
    L=fo.readline()

#9) delete a file and folder
import os
if os.path.exists('f11.txt'):
    os.remove('f11.txt')
    print("file named f11.txt is deleted successfully ")
else:
    print("file does not exist")
os.rmdir('Demo')
print("folder named Demo is deleted successfully ")
#10) remove duplicate lines from file
fo = open('f1.txt')
fi = open('f3.txt', 'w')
L = fo.readline()  # abc
L1 = []
while L:
    if L not in L1:
        L1.append(L)  # abc, def
    L = fo.readline()  # def, abc
fi.writelines(L1)
fo.close()
fi.close()
import os
os.remove('f1.txt')
os.rename('f3.txt', 'f1.txt')
