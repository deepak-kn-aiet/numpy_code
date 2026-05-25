import numpy as np
a1 = np.array([1,2,3,4,5,6,7,8,9,10])

a2 = a1.view()
print(f'original array: {a1}')
print(f'original array: {a2}')
a1[0]=100
print(f'original array: {a1}')
print(f'original array: {a2}')
a2 = a1.copy()
print(f'original array: {a1}')
print(f'original array: {a2}')
a1[0]=10
print(f'modified array: {a1}')
print(f'original array: {a2}')