# **26 What is the output of the following**
a = [1, 2, 3]
b = [4, 5, 6]
print([a, b])
print((a, b))

#________________________________*************___________________________________________
# **27 How to remove duplicates from the list without using inbuilt functions**
# >>> items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
items1=list(set(items))
print(items1)
         #_____________________#####SOLUTION2#########_______________________
res=[]
for i in items:
    if i not in res:
        res.append(i)
print(res)
                   #But it will still have 1 instance of the element

#________________________________*************___________________________________________
# **28 Find the longest word in the sentence**
s28='hi hello how are you. welcome'
a=s28.split()
res=s28[0]
for i in a:                        #Learn Sorted and Use Sorted
    if len(i)>len(res):
        res=i
print(res, len(res))
#________________________________*************___________________________________________
# **29 write a program to reverse the values in the dictionary if the value is of type String**
# >>> d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
d29={'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
for i in d29:
    if type(d29[i])==str:
        res=''
        for j in d29[i]:
            res=j+res
        d29[i]=res
print(d29)


#________________________________*************___________________________________________
# **30 write a program to get 1234
# t = ('1', '2', '3', '4')
t = ('1', '2', '3', '4')
res=0
for i in t:
    res=res*10+int(i)
print(res)