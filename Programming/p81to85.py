# **81 What is the difference between a list and a tuple**
"""1. The main difference between a list and a tuple is that list's are mutable and tuples are immutable.
2. Python over allocates memory for lists. The reason for over allocation of memory is to support append operation.
Where as in tuples, memory is not over allocated, as tuples does not support append operation.
(Since tuples are immutable, it does not support append operation).
3. Tuples are more memory efficient than lists. (because in tuples no extra memory is allocated. It is fixed).
4. Tuples are negligibly faster than lists.
"""
#________________________________*************___________________________________________
# **82 Write a program to print all the consonants in a given string**
s='abcdefghijklmn'
for i in s:
    if i.isalpha() and i not in 'aeiouAEIOU':
        print(i,end=' ')

# **83 Write a program to count the number of commented lines in a text file**

#________________________________*************___________________________________________
# **84 Write a program to check if the year is leap year or not**
""">>> import calendar
>>> print(calendar.isleap(2012))
>>> True
>>> print(calendar.isleap(2013))
>>> False
>>> print(calendar.isleap(2016))
>>> True
"""

# **85 Liner Search**
#It is nothing but the for loop.
