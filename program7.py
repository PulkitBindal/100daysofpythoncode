# Declaration of function and creating list from it.
# def listwrite(**a):
#     print(type(a))
#     li=[i for i in range (1,20,2)]
#     print(a)
#     return li

# print(listwrite(name='Pulkit',city='New York'))


# Declaration of function and creating a table of 5 using while loop - 

# def table(num):
#     for i in range(1,101):
#         if i==11:
#             break
#         print(num,"*",i,"=",(num*i))
# table(18)

# Playing with List

lt = [3,9,1,101,44,78,5]
print(lt)
lt.sort(reverse=True)
lt.sort()
print(lt)
lt1 = lt.copy()
lt1.append(1000)
lt1.extend(lt)
lt1.sort()
print(lt1)

# Factorial Program

def facto(a):
    if a == 1:
        return a
    elif a<=0:
        return "Either input is 0 or you have entered a negative Number"
    else:
        return a * facto(a-1)
print(facto(3))