# Declaration of List and Usage
l = []
l.append(4)
l.append(10)
print(l)
print(type(l))
#Declaration of Dictionary and usage 
d={}
d[4]="Four"
d[10]="Ten"
print(d)
print(type(d))
#Declaration of Set and Usage
s=set()
s.add(1)
s.add(3)
print(s)
print(type(s))
# Creating list via for loop
l=[i for i in range(1,10)] # Called as List Comprehension 1
print(l)
print(type(l))
lst=[i*i for i in range(10) if i%2==0] # Called as List Comprehension 2
print(lst) 
# Declaration of Tuple and Usage
t=tuple(l)
print(t)
print(type(t))