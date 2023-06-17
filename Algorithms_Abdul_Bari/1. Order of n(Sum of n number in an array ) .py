#Code for writhing order of 1 
# We are using for loop for the analysis
#Sum of n number in an array 

"""
Every for loop takes n+1 time complexity and the statement inside them takes
n time complexity.
Therefore the final time complexity comes out to be Order of n.
"""
A=[1,2,3,4]
sum =0
for i in range(len(A)) :
    sum = sum +A[i]


print("Sum of all element in an array is ",sum)

# Here we see the time complexity is O(n). 
