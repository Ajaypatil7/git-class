# **21 Write a class named Simple and it should have iteration capability.**
class Simple:
    def __init__(self,element):
        self.element=element
    def __iter__(self):
        return iter(self.element)
a=Simple([1,2,3,4,5])

#________________________________*************___________________________________________
# **22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a**

#________________________________*************___________________________________________
# **23 Write a python program to get the below output**
# sentence = "Hi How are you"
# o/p should be "iH woH era uoy"
s23="Hi How are you"
op23=''
a=s23.split()
for i in a:
    rev=''
    for j in i:
        rev=j+rev
    op23+=rev+' '
print(op23)

#________________________________*************___________________________________________
# **24 Write a python program to get the below output**
# sentence = "Hi How are you"
# o/p should be "ouy era woH iH"
s24="Hi How are you"
op24=''
for i in s24:
    op24=i+op24
print(op24)

#________________________________*************___________________________________________
# **25 Write a lambda function to add two numbers (a, b)**

res=lambda a,b : a+b
print(res(10,190))
