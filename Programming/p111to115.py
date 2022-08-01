# **111 Maximum sum of 3 numbers and Minimum sum of 3 numbers**
numbers = [10, 15, 20, 25, 30, 35, 40, 15, 15]
numbers.sort()
min_sum=numbers[0]+numbers[1]+numbers[2]
max_sum=numbers[-1]+numbers[-2]+numbers[-3]
print(max_sum, min_sum)


# **112 Write a program to get the output as below**
s="python@#$%pool$dgfh"
# o/p should be ['PYTHON', 'POOL']
op=[]
temp=''
for i in s:
    if i.isalnum():
        temp+=i.upper()
        continue
    if len(temp)!=0:
        op.append(temp)
        temp=''
else:
    op.append(temp)
print(op)


# **113 Write a program to print all the number which are ending with 5**
numbers = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']
for i in numbers:
    if int(i) %10==5:
        print(int(i))

# **114 Write a program to get the indexes of each item in the below list**
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# output should be -  {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}
op={}
i=0
while i <len(names):
    if names[i] not in op:
        op[names[i]]=[]
        op[names[i]].append(i)
    else:
        op[names[i]].append(i)
    i+=1
print(op)

# **115 Write a program to print "Bangalore" 10 times without using "for" loop**
def rep_string(s,n):
    if n==0:
        return
    print(s)
    rep_string(s,n-1)
rep_string('Bangalore', 10)
