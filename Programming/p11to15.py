# **11. Write a program to read a random line in a file. (ex. 50, 65, 78th line)**
def read_line(n):
    fobj=open("C:\\Users\\Admin\\Desktop\\practice.txt",'r')
    lines=fobj.readlines()
    print(lines[n-1])
read_line(2)
read_line(7)

# **12. Write a program to read random lines in a file. (ex. I want read all lines 10th to 15th line)**
def read_line(s,e):
    fobj=open("C:\\Users\\Admin\\Desktop\\practice.txt",'r')
    lines=fobj.readlines()
    for i in range(s,e+1):
        print(lines[i])
read_line(2,4)
read_line(7,9)
print("************************")
# **13 Program to print the last "N" lines of a file.**
def read_lastline(n):
    fobj=open("C:\\Users\\Admin\\Desktop\\practice.txt",'r')
    lastlines=fobj.readlines()
    for i in range(-1,-(n+1),-1):
        print(lastlines[i])

read_lastline(4)
read_lastline(7)


# **14. Write a program to check if the given string is Palindrome or not without using reversed method.**
s14='malayalam'
op14=s14[::-1]
if s14==op14:
    print('It is a Palindrome')


# **15 Write a program to search for a character in a given string and return the corresponding index.
s15='setuumdingdytauk'
ch=input('Enter the character to check')
cnt=0
for i in s15:
    if ch==i:
        print(cnt)
        break                             # THis can be solved using enumerate.
    if cnt==len(s15)-1:
        print(-1)
    cnt+=1
#Using while loop
i=0
while i<=len(s15):
    if s15[i]==ch:
        print(i)
        break
    if i==len(s15):
        print(-1)
    i+=1
