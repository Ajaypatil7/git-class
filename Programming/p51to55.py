# **51 Write a program to update the tuple**
# t1 = (1, 2, 3, 4)
# t2 = (100, 200, 300)
# o/p (1, 2, 3, 4, 100, 200, 300)
t1 = (1, 2, 3, 4)
t2 = (100, 200, 300)
op=t1
print(op)
for i in t2:
    op=op+(i,)
print(op)


#________________________________*************___________________________________________
# **52 Write a program to replace value present in nested dictionary.**
# d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# Replace "nose" with "net"
d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
for i in d:
    if type(d[i])==dict:
        for j in d[i]:
            if d[i][j]=='nose':
                d[i][j]='net'
    if d[i]=='nose':
        d[i]='net'
print(d)
#________________________________*************___________________________________________
# **53 Write a program to count the number of white spaces in a file.**
#________________________________*************___________________________________________
# **54 Grouping anagrams.**
#________________________________*************___________________________________________
# **55 What is the difference between default dict and normal dictionary.**
"""
Defaultdict
-----------
1. When each key is encountered for the first time, it will not be there in the mapping.
2. So an entry is automatically created with default value (an empty list in case of defaultdict of list and zero in case of defaultdict int).
3. When keys are encountered again, the look-up proceeds normally as like a normal dictionary.
4. So, in defaultdict, creation of key, initialisation will happen simultaneously. 

Normal Dictionary
------------------
1. In case of normal dictionary, if the key does not exist, "KeyError" is raised. 
2. In order to work on the value, first the key needs to be created and initialised.
"""