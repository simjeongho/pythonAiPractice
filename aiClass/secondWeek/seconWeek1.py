import numpy as np

a = np.array([1, 2, 3])  # Create a rank 1 array
print(type(a), a.shape, a[0], a[1], a[2])

# Change an element of the array
# [5 2 3]
# numpy의 내장 함수들 
a[0] = 5
print(a)
b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
print(b)

a = np.zeros((2,2))  # Create an array of all zeros
print(a) 

b = np.ones((1,2))   # Create an array of all ones
print(b)

c = np.full((2,2), 3) # Create a constant array
print(c)

d = np.eye(2)        # Create a 2x2 identity matrix
print(d)

e = np.random.random((2,2)) # Create an array filled with random values
print(e)
