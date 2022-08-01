# **66 Write a method that returns the last digit of an integer. For example, the call of
# get_last_digit(3572) should return 2.**
def get_last_digit(n):
    print(n%10)
get_last_digit(3572)
get_last_digit(0)
get_last_digit(89)

#________________________________*************___________________________________________
# **67 Write a program to find most common words in a given list.**
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes','the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not',
'around', 'the', 'eyes', "don't", 'look', 'around', 'the','eyes', 'look', 'into','my', 'eyes', "you're", 'under']
common=[words[0],0]
i=0
rep=[]
while i<len(words):
    if words[i] not in rep:
        count=0
        for j in words[i:]:              #Use Counter and in that use most common method.
            if words[i]==j:
                count+=1
    if common[1]<count:
        common[0],common[1]=words[i],count
    i+=1
print(common)



#________________________________*************___________________________________________
# **68 Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n and
# returns the last n elements from the given sequence, as a list.**

def tail(sequence, n):
    temp=[]
    i=len(sequence)-1
    while i>0 and n>0:
        temp.append(sequence[i])
        i-=1
        n-=1
    return temp
list1=tail('welcome to India', 5)
print(list1)
#________________________________*************___________________________________________
# **69 Write function named is_perfect_square that accepts a number and returns True if it's a
# perfect square and False if it's not.**
def is_perfect_square(n):
    if n==1:
        return True
    for i in range(1,n//2+1):
        if i*i==n:
            return True
    return False
print(is_perfect_square(49))

#________________________________*************___________________________________________
# **70 Write a program to get all the duplicate items and the number of times the item is repeated in the list.**
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
i=0
rep=[]
while i<len(names):
    if names[i] not in rep:
        count=0
        for j in names[i:]:
            if names[i]==j:
                count+=1
        if count>1:
            print(names[i],count)
    rep.append(names[i])
    i+=1