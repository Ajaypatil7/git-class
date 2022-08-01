# 131 What are .pyc files
#            1. pyc files are python compiled.
#            2. Once .py file is compiled by python compiler, it generates .pyc file.
#            3. .pyc files contains byte code which is understandable by python virtual machine.
#            4. pyc files are generated when a python module is imported.
#            5. Python compiler will not compile a python module again and again unless there is a change in code.
#            6. This makes programs to run faster since byte code for a module is already generated.

#132 Reverse a list without using any built-in functions and slicing
i=0
l1=[1,2,3,4,5,6]
j=len(l1)-1
while i<len(l1)//2:
    l1[i],l1[j]=l1[j],l1[i]
    i+=1
    j-=1
print(l1)

#133 Write a program to get the below output
    # i/p = "10.20.30.40"
    # o/p = "40.30.20.10"
s="10.20.30.40"
s=s.split('.')
s.reverse()
s='.'.join(s)
print(s)

#134 What is the difference between while loop and for loop.
# The body of while loop gets executed until some condition is True.
# Once the condition if False, the control comes out of the while loop.

# The body of for loop get executed for some fixed number of iterations.

# 135 What are magic methods?
#    Magic methods are special methods which starts and ends with double underscores.
#    (they are also called as dunders)
#    Magic methods are internally called by python. We can customize the behaviour of an object or class
#    using magic methods.
#    They are also called as protocols.

#    e.g. when you ask for the length of the list len(names) internally python will call __len__ method on list object.

#    e.g. when you check for membership "apple" in names python internally triggers __contains__("apple")



