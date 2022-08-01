# 141 What is the difference between a module, a package, and a library
#            1. A module is simply a Python file that’s intended to be imported into scripts or other modules.
#               It contains functions, classes, and global variables.

#  2. A package is a collection of modules that are grouped together inside a folder to provide consistent
#     functionality. Packages can be imported just like modules. They usually have an __init__.py file in them.

#    3. A library is a collection of packages.

# 142 write a program to get the below output using while loop
#
#            1
#            12
#            123
#            1234

i,n=1,4
while i<=n:
    j=1
    while j<=n:
        if i>=j:
            print(j, end='')
        else:
            print('',end='')
        j+=1
    print()
    i+=1

# 143 write a program to get the below output
#   items = ['$123.45', '$434.23', '$567.89']
#   # o/p [123.45, 434.23, 567.89]

# 144 Generator function for Fibonacci series program

# 145 Write a program to print common character present in all the items of the below list
items = [ "glory", "glass", "sight", "fight"]
item=items[0]
for i in item:
    flag=True
    for j in items:
        if i not in j:
            flag=False
            break
    if flag==True:
        print(i)

# 146 Function should accept a list and if any number divisible by 3 then modify to 33 or else keep it as it is
def modify(a):
    i=0
    while i<len(a):
        if a[i]%3==0:
            a[i]=33
        i+=1
    print(a)


modify([1,2,3,4,5,6,7,8,9])


# 147  write a program to print the below pattern
#
#            1 2 3 *
#            1 2 * 4
#            1 * 3 4
#            * 2 3 4
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print('*',end=' ')
        else:
            print(j, end=' ')
    print()
