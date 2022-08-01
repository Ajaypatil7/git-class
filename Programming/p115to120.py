# **116 Write a program to print all the words which starts with letter 'h' in the given string**
string = 'hello world hi hello universe how are you happy birthday'
for i in string.split(' '):
    if i[0]=='h':
        print(i)


# **117 Write a program to sum all even numbers in the given string**
sentence = 'hello 123 world 567 welcome to 9724 python'
sum=0
for i in sentence:
    if i.isdigit() and int(i)%2==0:
        sum=sum+int(i)
print(sum)

# **118 Write a program to add each number in word1 to number in word2**
word1 = 'hello 1 2 3 4 5'
word2 = 'world 5 6 7 8 9'
# e.g. 1 + 5, 2 + 6, 3 + 7, 4 + 8, 5 + 9

# **119 Write a program to filter out even and odd numbers in the given string**
sentence = 'hello 123 world 456 welcome to python498675634'
even=''
odd=''
for i in sentence:
    if i.isdigit():
        if int(i)%2==0:
            even+=i
        else:
            odd+=i
print(even, odd)
# **120 Write a program to print all the number which are starting with 8**
numbers = ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']
for i in numbers:
    if i[0]=='8':
        print(i)
        