# 16. Write a program to get the below output
sentence = "hello world welcome to python programming hi there"
# d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
words=sentence.split()
d={}
for i in words:
    if i[0] not in d:
        d[i[0]]=[i]
    else:
        d[i[0]].append(i)
print(d)

# **17 Write a program to replace all the characters with - if the character occurs more than once in a string**
# my_string = 'hellohai' # O/P should be '-e--o-ai'
s17= 'hellohai'
op17=''
for i in s17:
    if s17.count(i)>1:
        op17=op17+'-'
    else:
        op17+=i
print(op17)

#-------sol2-------------
for i in s17:
    cnt=0
    for j in s17:
        if i ==j:
            cnt+=1
    if cnt>1:
        op17=op17+'-'
    else:
        op17+=i
print(op17)
#________________________________*************___________________________________________

# **18 write a decorator that returns only positive values of subtraction**
# use abs function
def positive(func):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        res=abs(res)
    return wrapper

@positive
def sub(*args,**kwargs):
    for i in args:
        if i==args[0]:
            res=i
        else:
            res-=i
    return res
sub(1,2,3)
#________________________________*************___________________________________________
# **19 How to get the count of the number of instances of a class that is being created.**
class Sample:
    count=0
    def __init__(self):
        Sample.count+=1
a=Sample()
b=Sample()
c=Sample()
print(Sample.count)

#________________________________*************___________________________________________
# **20 Write a function which takes a list of strings and integers.If the item is a string it should print as
# is and if the item is integer or float it should reverse it.**
def list1(a, op20=[]):
    for i in a:
        if type(i) ==str:
            op20.append(i)
        elif type(i)==int:
            rev = 0
            while i>0:
                res=i%10
                i=i//10
                rev=rev*10+res
            op20.append(rev)
    print(op20)

list1(['ajay',103456,'abhay', 221096,3456, 'aryan'])