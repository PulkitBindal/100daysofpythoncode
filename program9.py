# Declaration of f-strings and finally printing.
firststr="Pulkit"
secondstr="Goa"

print(f"Hey all, I am {firststr} and I am from {secondstr}")
print(f"Hey all, I am {{firststr}} and I am from {{secondstr}}") # Normal Code
print("Hey all, I am {firststr} and I am from {secondstr}") # Optimized Code


# Usage of Doc String 

def square(r):
    '''Use this function to do square of any number/argument'''
    return r**2
print(square(4))
print(square.__doc__)
