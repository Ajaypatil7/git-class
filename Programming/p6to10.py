# **6. Write a program to print alternate characters in a string.**
s6='abcdefghijkl'
res6=''
i=0
while i<len(s6):
    if i%2==1:
        res6+=s6[i]
    i+=1
print(res6)
print(s6[::2])

# **7. Write a Program to print ascii values of the characters present in a string.**
s7='abcd'
for i in s7:
    print(ord(i), end=' ')

# **8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.**
s8='ABCD efgh'
res8=''
for i in s8:
    if 'a'<=i<='z':
        res8+=chr(ord(i)-32)
    elif 'A'<=i<='Z':
        res8 += chr(ord(i) +32)
    else:
        res8+=i
print(res8)


# **9. Write a program to swap two numbers without using the 3rd variable.**
a,b=10,20
a=a+b
b=a-b
a=a-b
print(a,b)
a,b=b,a


# **10. Write a program to merge two different lists.**
a=[1,2,3,4,5]
b=[5,6,7,1,2]
c=a+b
print(c)
# d=[]
# for (i, j) in (a,b):
#    print(i,j)
# 
# print(d)
