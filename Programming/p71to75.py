# **71 Write a program to count the number of occurrences of each word in a file.**

#________________________________*************___________________________________________
# **72 Write a program to count the number of occurrences of vowels in a file.**

#________________________________*************___________________________________________

# **73 Write a program to print all numeric values in a list**
items = ['apple', 1.2, 'google', '12.6', 26, '100']
for i in items:
    if type(i) in (int , float):
        print(i)

#________________________________*************___________________________________________
# **74 Triangle Patterns**
# *
# * *
# * * *
# * * * *
# * * * * *
n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        if row >=col:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col>=n+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col>=n+1:
            print('*', end=' ')
        else:
            print(' ', end='')
    print()
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col<=n+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
# * * * * * *
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *
for row in range(1,n+1):
    for col in range(1,n+1):
        if row<=col:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#  * * * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *
for row in range(1,n+1):
    for col in range(1,n+1):
        if row<=col:
            print('*', end=' ')
        else:
            print(' ', end='')
    print()
# 1
# 12
# 123
# 1234
# 12345
for row in range(1,n+1):
    for col in range(1,n+1):
        if row>=col:
            print(col, end='')
        else:
            print(' ', end='')
    print()
#     1
#    12
#   123
#  1234
# 12345
for row in range(1,n+1):
    k=1
    for col in range(1,n+1):
        if row+col>=n+1:
            print(k, end='')
            k+=1
        else:
            print(' ', end='')
    print()
#      1
#     1 2
#    1 2 3
#   1 2 3 4
#  1 2 3 4 5
for row in range(1,n+1):
    k=1
    for col in range(1,n+1):
        if row+col>=n+1:
            print(k, end=' ')
            k+=1
        else:
            print(' ', end='')
    print()


#________________________________*************___________________________________________
# **75 Write a program count the occurrence of a particular word in the file**
