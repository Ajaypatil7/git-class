def dict1(*args):
    print(args)

dict1({'a':1, 'b':2})

x=[1,2,3,4]
y=[11,22,33,44]

for i,j in [*x,*y]:
    print(i,j)