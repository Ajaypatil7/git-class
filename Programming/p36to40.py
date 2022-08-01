# **36 Sum all the numbers in the below string.**
# s = "Sony12India567Pvt2ltd"             They are asking numbers NOT NUMERIC VALUES. means 12+567+2
s36 = "Sony12India567Pvt2ltd"
res=0
for i in s36:
    if '0'<=i<='9':
        res=res+int(i)
print(res)
#________________________________*************___________________________________________
# **37 Write a program to sum all the numbers in below string.**
# s = "Sony12India567Pvt2ltd" # eg.12+567+2
s37 = "Sony12India567Pvt2ltd"
res=0
i=0
while i<len(s37):
    temp=''
    if '0' <= s37[i] <= '9':
        for j in s37[i:]:
            if not('0' <= j <= '9'):
                break
            temp += j
        i+=len(temp)
        res+=int(temp)
    i+=1
print(res)




#________________________________*************___________________________________________
# **38 Print all the numbers in the below list**
# a = ['abc', '123', 'hello', '23']
a = ['abc', '123', 'hello', '23']
for i in a:
    flag=True                          #we can use isdigit() also
    for j in i:
        if not('0' <= j <= '9'):
            flag=False
    if flag==True:
        print(i)

#________________________________*************___________________________________________
# **39 Program to print the number of occurrences of characters in a String without using inbuilt functions.**
s39='Hello Hii Welcome How are You'
res=''
temp=''
i=0
while i<len(s39):
    if s39[i] not in temp:               #Use the default dictionary concept
        temp+=s39[i]
        count=0
        for j in s39[i:]:
            if s39[i]==j:
                count+=1
        print(s39[i], count)
    i+=1

#________________________________*************___________________________________________
# **40 Program to print only the repeated characters and count of the same.**
s40='Hello Hii Welcome How are You'
res=''
temp=''
i=0
while i<len(s39):
    if s39[i] not in temp:
        temp+=s39[i]
        count=0
        for j in s39[i:]:
            if s39[i]==j:
                count+=1
        if count>1:
            print(s39[i], count, "***")
    i+=1