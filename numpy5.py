import numpy as np
a = np.array([-3, -2, -1, 0, 1, 2, 3,4,5,6 ,7,8,9])
# square root of each element in the array
print(np.sqrt(a))
#absolute value 
print(np.abs(a))
#nim/max
print(np.max(a))
print(np.min(a))
#mean
print(np.mean(a))
np2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.max(np2[0:3,0:3]))
print(np.abs(np2[0:1,0:2]))
# similar for sin and cos
print(np.sin(a))
print(np.cos(a))
#logarithm
print(np.log(a))