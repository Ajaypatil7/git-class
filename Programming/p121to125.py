# 121 Write a program to remove duplicates from the list without using set or empty list
l1 = [3,1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]
i=len(l1)-1
while i>=0:
    if l1[i] in l1[:i]:
        l1.pop(i)
    i-=1
print(l1)

#122 Print all the missing numbers from 1 to 10 in the below list
list1=[1,2,4,5,7,8,10]
for i in range(1,11):
    if i not in list1:
        print(i)

# ** 123 Write a python program to get the below output**
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
# o/p ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
op=[]
for i in l1:
    for j in l2:
        op.append(f'{i}{j}')
print(op)



# 124 Write a python program to get the below output



# **125 What is the output of the below function call**
class Demo:
    def greet(self):
        print("hello world")

    def greet(self):
        print("hello universe")

d = Demo()
d.greet()

#op:- 'Hello Universe'