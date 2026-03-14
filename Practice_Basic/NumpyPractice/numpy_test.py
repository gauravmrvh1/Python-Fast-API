import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(np.__version__ )
print(arr)
print(type(arr))


arr = np.array((1, 2, 3, 4, 5))
print(arr)
print(type(arr))



arr = np.array(42)
print(arr)
print(arr.ndim)


arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.ndim)

arr = np.array([
    [1, 2, 3], [4, 5, 6]
])
print(arr)
print(arr.ndim)

arr = np.array([
    [
        [1, 2, 3], [4, 5, 6]
    ],
    [
        [1, 2, 3], [4, 5, 6]
    ]
])
print(arr)
print(arr.ndim)


arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)