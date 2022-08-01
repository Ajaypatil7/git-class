# **101 Count number of words in a sentence. ignore special characters.**
sentence = "Hi there! How are you:) How are you doing today!"
s=sentence.split(' ')
print(len(s))

# **102 Grouping even and odd numbers**
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# o/p should be {1: [1, 3, 5, 7, 9], 0: [2, 4, 6, 8, 10]}
dict={0:[],1:[]}
for i in numbers:
    if i%2==0:
        dict[0].append(i)
    else:
        dict[1].append(i)
print(dict)
# **103 Find all max numbers from the below list**
numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
max=numbers[0]
for i in numbers:
    if i>=max:
        max=i
for j in numbers:
    if j==max:
        print(j)



# **104 Find all max length words from the below sentence**
sentence = "hello world hi apple you yahoo to you"
list=sentence.split(' ')
max_length=len(list[0])
for i in list:
    if len(i)>max:
        max=len(i)
for j in list:
    if len(j)==max:
        print(j)

# **105 Find the range from the following string**
# >>> sentence = '0-0, 4-8, 20-20, 43-45'
# output Should be [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
