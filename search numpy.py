import numpy as np
np1 = np.array([3,9,8,0,1,2])
x = np.where(np1 == 8)
print(x)
print(x[0])
print(np1[x[0]])
 
 # return even items
y = np.where(np1 % 2 == 0)
print(y)
print(np1[y])
print(y[0])

# return odd
z = np.where(np1 % 2 == 1)
print(z)
print(np1[z])
print(z[0])
