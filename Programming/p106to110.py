# ** 106 Can we override a static method in python? **
'''
class Parent:
    @staticmethod
    def demo():
        print('Running demo in Parent')


class Child(Parent):
    @staticmethod
    def demo():
        print('Running demo in Child')

>> > c = Child()
>> > c.demo()
>> > Running demo in Child
'''
# ** 107 Write a function which returns the sum of lengths of all the iterables **
# total_length([1, 2, 3], (4, 5), ['apple', 'google', 'yahoo', 'gmail', 'flipkart'], {1, 2, 3}, {'a': 1, 'b': 2})
# 15
def total_length(*a):
    sum=0
    for i in a :
        sum+=len(i)
    print(sum)
total_length([1, 2, 3], (4, 5), ['apple', 'google', 'yahoo', 'gmail', 'flipkart'], {1, 2, 3}, {'a': 1, 'b': 2})


# ** 108 Replace whitespaces  with newline character in the below string **
sentence = "Hello world welcome to python"
sentence=sentence.replace(' ', '\n')
print(sentence)


# ** 109  Replace  all vowels with "*"
sentence = "hello world welcome to python"
op=''
for i in sentence:
    if i in 'aeiouAEIOU':
        op+='*'
    else:
        op+=i
print(op)

# ** 110 Replace all occurances of "Java" with "Python" in a file **