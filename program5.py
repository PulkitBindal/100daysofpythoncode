#Given String and Outputting the Data in the form of Lists
st="PULKIT"
l=[]
print(type(st))
print(l)
for i in range(len(st)):
    l.append(st[i])
print(l)

#Declaration and usage of Lambda Function
a = lambda x , y , z , b , j : (((x * y) + z ) / (b + j))
print(a(3,4,8,6,4))

#Declaration of String and Outputting the Slice (Quick Quiz)
p = "Harry"
print(p[-4:-2]) # Result should be ar