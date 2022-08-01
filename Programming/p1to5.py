# **1. Write a program to find the length of the string without using inbuilt function (len)**
s='abcdefghijkl'
count=0
for i in s:
    if i:
        count+=1
print(count)

# **2. Write a program to reverse a string without using any inbuilt functions.**
rev=''
for i in s:
    rev=i+rev
print(rev)


# **3. Write a program to replace one string with another. e.g. "Hello World" replaces "World" with "Universe".**

s='hello world'
s=s.replace('world', 'universe')
print(s)



# **4. How to convert a string to a list and vice-versa.**
s='hello world'
l1=list(s)
print(l1)
print(''.join(l1))



# **5. Convert the string "Hello welcome to Python" to a comma separated string.**
s5="Hello welcome to Python"
op5=''
for i in s5:
    if i==' ':
        op5=op5+','
    else:
        op5+=i
print(op5)

print(s5.replace(' ', ','))