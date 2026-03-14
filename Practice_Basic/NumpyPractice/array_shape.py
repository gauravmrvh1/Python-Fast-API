import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newArr = arr.reshape(4, 3)
# print(newArr)


newArr = arr.reshape(2, 3, 2)
# print(newArr)


newArr = arr.reshape(2, 2, -1)
# print(newArr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
newArr = arr.reshape(-1)
print(newArr)