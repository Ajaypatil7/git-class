# **96 Write a program to sort a list which has mix of both odd and even numbers, in the sorted list,
# odd numbers should be in ascending order and even numbers should be in descending order**
a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
# >>> # o/p should be [1, 3, 7, 9, 11, 12, 8, 6, 4, 2]
list2,op=[],[]
for i in a :
    if i%2==0:
        list2.append(i)
    else:
        op.append(i)
op.sort()
list2.sort(reverse=True)
op.extend(list2)
print(op)

# **97 Write a program to count the number of occurrences of non-special characters in a given string**
s = 'Hello@world! welcome!!! Python$ hi how are you & where are you?'
count=0
for i in s:
    if i.isalnum():
        count+=1
print(count)

# **98 Grouping Flowers and Animals in the below list**
# items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']

# **99 Grouping files with same extensions**
# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']

# **100 Filter only those characters except digits**
s = '@hello12world34welcome!123'
print(list(filter((lambda i :not(i.isdigit())),s)))