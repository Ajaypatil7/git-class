# **91 What is the difference between append() and extend() method in list**
"""
# 1. append() method appends one item at the end of the list.
# 2. extend() method appends all the items of the iterable to the end of the list.
# 3. Both append() and extend() method's mutates the existing list.

# e.g.
# >>> a = [1, 2, 3]
# >>> b = (4, 5, 6)
# >>> a.extend(b)
# >>> a
# [1, 2, 3, 4, 5, 6]

# >>> c = {7, 8, 9}
# >>> a.extend(c)
# >>> a
# [1, 2, 3, 4, 5, 6, 8, 9, 7]
#
# >>> d = {'a': 1, 'b': 2, 'c': 3}
# >>> a.extend(d)
# >>> a
# [1, 2, 3, 4, 5, 6, 8, 9, 7, 'a', 'b', 'c']
#
# The list "a" is getting mutated each time when it is extended.
"""

# **92 Write a program to find the first repeating character in a string**
s='ello Hi how are you'
i=0
while i<len(s):
    if s[i] in s[i+1:]:
        print(s[i])
        break
    i+=1
# **93 Write a program to find the index of nth occurrence of a sub-string in a string**
# >>> sentence = "hello world welcome to python hello hi how are you hello there"
# >>> index_nth_occurance(sentence, 'hello', 3)
# >>> Start Index: 51, End Index: 56

# **94 Write a program to print prime numbers from 1 to 50**

# **95 Write a program to sort a list which has mix of both odd and even numbers, the sorted list
# should have odd numbers first and then even numbers in sorted order**
a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
#>>> # o/p should be [1, 3, 7, 9, 11, 2, 4, 6, 8, 12]
list2,op=[],[]
for i in a :
    if i%2==0:
        list2.append(i)
    else:
        op.append(i)
op.sort()
list2.sort()
op.extend(list2)
print(op)


