# **126 In the list below, find all the number pairs which results in 10 either when added or subtracted**
a = [3, 5, -4, 8, 11, 1, -1, 6]
i=0
while i<len(a):
    for j in a[i+1:]:
        if a[i]+j==10 or a[i]-j==10:
            print(a[i], j)
    i+=1
# **127 Write a decorator to prefix +91 to the original phone numbers**



# **128 Write a program to get the below output**
d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# >>> # o/p should be ['b', 'd']
op=[]
for i in d:
    if d[i]%2==0:
        op.append(i)
print(op)


# 129 Can we have multiple __init__ methods in a class
# Yes we can have multiple __init__ methods in a class.
# But the last __init__ method will override all the previous __init__ methods.

# 130 Why python is Object Oriented
#     Python is object oriented because everyting in python is an object (defined as class)