# **56 Explain property decorator in python.**


#________________________________*************___________________________________________

# **57 What is Mutable and Immutable datatypes.**
# ```python
"""
1. Mutable datatypes are objects whose value can be changed after creation. e.g. list, dict, set, user defined classes.
2. Immutable datatypes are objects whose value can not be changed after creating. e.g. int, float, bool, tuple, namedtuple
"""
#________________________________*************___________________________________________


# **58 Explain get() method in dictionaries.**

"""
point =  {'a': 1, 'b': 2}
1. Values of dictionary can be accessed in two different ways. using square bracket syntax and the other one is using get() method.
2. When we try to access a key of a dictionary which does not exist using square bracket syntax (point['c']), "KeyError" exception is raised.
3. When we try to access a key of a dictionary which does not exist using get() method (point.get('c')), None is returned and no exception is raised.
4. We can pass a positional argument to get() method as custom message, so that get() method returns the custom message if the key does not exist.
           e.g. profile.get('c', 'Sorry the key does not exist')
"""
#________________________________*************___________________________________________

# **59 Write a list comprehension to get a list of even numbers from 1-50**
b=[i for i in range(1,51) if i%2==0]
print(b)
#________________________________*************___________________________________________

# **60 Find the longest non-repeated substring in the below string**
