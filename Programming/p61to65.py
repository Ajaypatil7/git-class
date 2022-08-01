# **61 Write a program to find the duplicate elements in the list without using inbuilt functions**
names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
i=0
rep=[]
while i<len(names):
    if names[i] not in rep and names[i] in names[i+1:]:
        print(names[i])
    rep.append(names[i])
    i+=1

#________________________________*************___________________________________________
# **62 Write a program to count the number occurrences of each item in the list without using any inbuilt functions**
# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
i=0
rep=[]
while i<len(names):
    if names[i] not in rep:
        count=0
        for j in names[i:]:
            if names[i]==j:
                count+=1
        print(names[i], count)
    rep.append(names[i])
    i+=1

#________________________________*************___________________________________________
# **63 Write a function to check if the number is Prime**
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(is_prime(11))
print(is_prime(18))
#________________________________*************___________________________________________
# **64 How to create a tuple of numbers from 0 to 10 using range function**
t=tuple([a for a in range(1,11)])
print(type(t), t)

#or
tuple(range(1,11))
#________________________________*************___________________________________________
# **65 Write a program to find the largest number in the list without using any inbuilt functions**
list1=[1,2,3,4,3,2,76,8,11,66,44,55]
greatest=list1[0]
for i in list1:
    if i>greatest:
        greatest=i
print(greatest)
