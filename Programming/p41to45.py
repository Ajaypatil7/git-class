# **41 Write a program to get alternate characters of a string in list format.**
s41='abcdefghijkl'
i=0
list41=[]                      #we can also use slicing concept
while i<len(s41):
    if i%2==0:
        list41.append(s41[i])
    i+=1
print(list41)
#________________________________*************___________________________________________
# **42 Write a program to get square of list of number's using lambda function .**
square=lambda a: a*a
res=map(square, [1,2,3,4,5])
print(list(res))

#________________________________*************___________________________________________
# **43 Write a function that accepts two strings and returns True if the two strings are anagrams of each other.**
def anagram(a,b, flag=True):
    if len(a)==len(b):
        for i in a:
            if i not in b :
                flag=False
                break
        for j in b:
            if j not in a:
                flag=False
                break
        return flag
    else:
        return False

print(anagram('care','race' ))
print(anagram('ajay', 'jayt'))
#________________________________*************___________________________________________
# **44 Write a program to iterate through list and build a new list, only if the items of the list has even number
# of characters.**
# >>> names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
list44=[]
for i in names :
    if len(i)%2==0:
        list44.append(i)
print(list44)



#________________________________*************___________________________________________
#**45 Write a program to iterate through list and build a new dictionary, only if the items of the
# list has even number of characters.**
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
list45=[]
for i in names :
    if len(i)%2==1:
        list45.append(i)
print(list45)


