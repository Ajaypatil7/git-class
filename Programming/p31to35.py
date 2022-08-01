# **31 How to get the elements that are in list b but not in list a**
# a = [1, 2, 3]
# b = [1, 2, 3, 4]
a = [1, 2, 3]
b = [1, 2, 3, 4]
for i in b:                    #we can convert it to set and use difference method.
    if i not in a:
        print(i)

#________________________________*************___________________________________________

# **32 A function takes variable number of positional arguments as input.
# How to check if the arguments that are passed are more than 5**
def func1(*args):
    if len(args)>=5:
        print('It have more than 5 aguments')
    else:                                           #Keep in mind about kwargs
        print('function have less than 5 arguments' )
func1(1,2,3,4,5)
func1(1,2,3)

#________________________________*************___________________________________________
# **33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
# Assume Below is the contents of the log file

# lines = """CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical"""

#________________________________*************___________________________________________
# **34 Write a function to reverse any sequence without using reverse function.


#________________________________*************___________________________________________
# **35 Write a function to print the below output.**
# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX
def func(a,p):
    while p<len(a):
        print(a[p-1],end='')
        p+=2
    print()
func('TRACXN',0)
func('TRACXN',1)

#SOL2:-
def func(a,p):
    if p==0:
        return a[1::2]
    elif p==1:
        return a[0::2]
print(func('TRACXN',0))
print(func('TRACXN',1))