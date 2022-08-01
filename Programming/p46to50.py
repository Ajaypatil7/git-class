# **46 Write a program which squares the numbers in a list using map object**
# a = [1, 2, 3, 4, 5]
b=[1,2,3,4,5]
print(list(map(lambda a:a*a, b)))
#________________________________*************___________________________________________
# **47 Count number of lines in a file without loading the file to the memory**
# don't store the lines in datatype' that means they are not loaded
#________________________________*************___________________________________________
# **48 Printing line and line no's**
# use enumerate function

#________________________________*************___________________________________________
# **49 Write a Program to print the sum of entire list and sum of only internal list**
# l = [[1,2,3],[4,5,6],[7,8,9]]
l = [[1,2,3],[4,5,6],[7,8,9]]
all_sum=0
list_sums=[]
for i in l:
    if type(i)==list:
        add=0
        for j in i:                #use sum function
            all_sum+=j
            add+=j
        print(add)
        list_sums.append(add)
    else:
        list_sums+=i
print(all_sum,list_sums)
#________________________________*************___________________________________________
# **50 Write a program to reverse the list as below**
# words = ["hi", "hello", "python"]
op= ['python', 'hello', 'hi']