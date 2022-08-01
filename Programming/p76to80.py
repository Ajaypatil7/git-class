# **76 Write a program to map a product to a company and build a dictionary with company and list of products pair**
# >>> all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows',
#                 'iOS', 'Google Drive', 'One Drive']
# >>> # Pre-defined products for different companies
# >>> apple_products = {'iPhone', 'Mac', 'iWatch'}
# >>> google_products = {'Gmail', 'Maps', 'Google Drive'}
# >>> msft_products = {'Windows', 'One Drive'}
#SOLUTION
# all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows',
#                 'iOS', 'Google Drive', 'One Drive']
# apple_products = {'iPhone', 'Mac', 'iWatch'}
# google_products = {'Gmail', 'Maps', 'Google Drive'}
# msft_products = {'Windows', 'One Drive'}
# company=[apple_products,google_products,msft_products]
# dict1={}
# i=0
# while i<len(company):
#     list1=[]
#     for j in all_products:
#         if j in company[i]:
#             list1.append(j)
#     dict1[str(i)]=list1
#     i+=1
# print(dict1)

#________________________________*************___________________________________________
# **77 Write a program to rotate items of the list**
names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
i=0
j=len(names)-1
temp=names[j]
while i<=j:
    names[i],temp=temp,names[i]
    i+=1

print(names)

#________________________________*************___________________________________________
# **78 Write a program to rotate characters in a string**
# s='abcdefgh'
# i=0
# j=len(s)-1
# while i<len(s)//2:
#     s[i],s[j]=s[j],s[i]
#     i+=1
#     j += 1
# print(s)

#________________________________*************___________________________________________
# **79 Write a program to count the number of white spaces in a given string**
s='    abcd     fsihk   '
cnt=0
for i in s:
    if i==' ':
        cnt+=1
print(cnt)

print(s.count(' '))

#________________________________*************___________________________________________
# **80 Write a program to print only non-repeated characters in a string**
s='Hai Hii How are You'
rep=''
i=0
while i<len(s):
    if s[i] not in rep and s[i] not in s[i+1:]:
        rep+=s[i]
    i+=1
print(rep)