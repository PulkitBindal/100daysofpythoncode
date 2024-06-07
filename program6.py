#Declaration of a varibale and running a while loop
count = 4
while (count > 0):
    print(count)
    count = count - 1

# Declaration of a function and use of it. 
def gmean(a,b):
    mean=((a+b)/2)
    print (mean)
a=2
b=3
gmean(a,b)

# Declaration of a function and use of it #2.
def avgvalue(x,y,z):
    average = ((x+y+z)/3)
    print(average)
avgvalue(1,2,3)

# Declaration of a function and passing the parameter using *. To make it as Tuple.

def average(*numbers):
    sum = 0 
    for i in numbers: # here i will not be 0,1,2,3, and so on.... 
        sum = sum + i # It will be 2,3,4,5 same as tuple. i=2, then i=3, then i=4 and so on.
        print(i)
        print(type(numbers))
average(8,9,10,11)

# Declaration of a function and passing the parameter using **. To make it as Dictionary.

def pt(**name):
    print(type(name))
    print(name)
pt(a="One",b="Two",c="Three")

# Declaration of a function and take value using return keyword 

def add(a,b):
    sum=0
    sum=a+b
    return sum
print(add(4,6))