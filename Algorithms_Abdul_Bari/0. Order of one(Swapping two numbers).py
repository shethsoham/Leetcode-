# Order of 1 (Unit)
# Swapping of 2 elements 
"""
Every simple step in algorithm takes 1 unit 
"""


a=input("Enter the value of a")
b=input("Enter the valur of b")

def swap(a,b):
       
    temp = a 
    a=b
    b=temp
    return a,b

a, b = swap(a,b)
print ("a =",a)
print("b=",b)

# Here the code is in order of 1 i.e O(1)