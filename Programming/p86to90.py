# ** 86 Difference between xrange and range **
"""
# python2- xrange
# python3- range

# 1. xrange does not stop, start and step attributes. But range object has start, stop and step attributes.
#   Python-3
#   r = range(0, 10)
#   r.start
#   r.stop
#   r.step

#   r = xrange(0, 10)
#   In Python-2 The above attributes are not supported.
#
# 2. range Object supports slicing! But xrange does not support slicing
#
# 3. range object has __contains__ method implemented. So it supports membership testing.
#    But xrange does not implement __contains__ method.
#    So Python will iterate over each and every item in the range xrange object until it finds a match.
#    (So if you are searching for a number in range is faster than xrange)
#
# 4. range will accept integer of any size. But xrange objects accepts integer size equivalent to C long!
"""
# **87 Write a program to count no of capital letters in a string**
s='SRDTFHGitrd23456agyjs'
cnt=0
for i in s:
    if i.isupper():
        cnt+=1
print(cnt)
# **88 Write a program to get the below output**

# *
# * *
# *
# * * *
# *
# * * * *
# *
# * * * * *
n=8
k=2
for row in range(1,n+1):
    if row%2==1:
        print('*')
    elif row%2==0:
        print('* '*k)
        k+=1



# **89 Write a program to get the below output**
# >>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# o/p:
# >>> [1, 2]
#     [3, 4]
#     [5, 6]
#     [7, 8]
#     [9]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i=0
list1=[]
while i<len(a):
    if len(list1)==2:
        print(list1)
        list1=[]
    list1.append(a[i])
    i+=1
 print(list1)



# **90 Write a program to check if the elements in the second list is series of continuation of
# the items in the first list**
a = [10, 12, 14, 16, 18]
b = [20, 22, 24, 26, 28]

a1 = [0, 5, 10, 15]
b1= [20, 25, 30, 35, 40]

x = [10, 20, 30, 40]
y = [50, 40, 60, 70]
def is_series(list1,list2):
    list1.extend(list2)
    const=list1[0]-list1[1]
    i=0
    while i<len(list1)-1:
        if list1[i]-list1[i+1]!=const:
            return False
        i+=1
    return True
print(is_series(a,b))
print(is_series(a1,b1))