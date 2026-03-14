import numpy as np
from numpy import random

x = random.randint(100)
# print(x)

x=random.randint(100, size=(5))
# print(x)


x = random.randint(100, size=(3, 5))
# print(x)


x = random.rand(5)
# print(x)


x = random.choice([3, 5, 7, 9])
# print(x)


x = random.choice([3, 5, 7, 9], size=(3, 5))
# print(x)


arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)