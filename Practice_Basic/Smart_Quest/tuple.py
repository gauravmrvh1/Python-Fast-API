# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# | Feature        | List                               | Tuple                          |
# | -------------- | -------------------------------    | ------------------------------ |
# | Syntax         | `[ ]`                              | `( )`                          |
# | Mutability     | ✅ Mutable (change ho sakta hai)   | ❌ Immutable (change nahi hota) |
# | Performance    | Thoda slow                         | Faster                         |
# | Memory         | Zyada use                          | Kam use                        |
# | Methods        | Many (append, remove, etc.)        | Limited                        |
# | Use case       | Dynamic data                       | Fixed data                     |
# | Hashable       | ❌ No                              | ✅ Yes (if elements immutable)  |
# | Dictionary key | ❌ No                              | ✅ Yes                          */



t = ("gaurav", 2 , 2, [1,2,3], {"name" : "gaurav", "mobile": 8881438098})
print(t)
# t[0] = "gaurav marvaha" # This will give an error because tuple is unchangeable
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[3][1])
print(t[3].append(4))
print(t[3])
print(t[4])
print(t[4]["name"])
print(t[4]["mobile"])


# Tuple Methods
print(t.count(2)) # This will count the number of times 2 is present in the tuple
print(t.index("gaurav")) # This will give the index of the first occurrence of  "gaurav" in the tuple



# Packing and Unpacking of Tuple
# Packing
a = 1
b = 2
c = 3
t1 = a, b, c
print(t1)

# Unpacking
a1, b1, c1 = t1
print(a1)
print(b1)
print(c1)

# Nested Tuple
t2 = (1, 2, (3, 4), 5)
print(t2)
print(t2[2])
print(t2[2][0])
print(t2[2][1])

# Tuple Concatenation
t3 = (1, 2, 3)
t4 = (4, 5, 6)
t5 = t3 + t4
print(t5)

# Tuple Repetition
t6 = t3 * 2
print(t6)

# Tuple Slicing
t7 = (1, 2, 3, 4, 5)
print(t7[1:4]) # This will give a new tuple with elements from index 1 to 3
print(t7[:3]) # This will give a new tuple with elements from index 0 to 2
print(t7[3:]) # This will give a new tuple with elements from index 3 to the end
print(t7[1:4:2]) # This will give a new tuple with elements from index 1 to 3, with a step of 2

# Tuple Length
print(len(t7)) # This will give the length of the tuple

# Tuple Membership
print(3 in t7) # This will return True if 3 is present in the tuple, otherwise False
print(6 in t7) # This will return False because 6 is not present in the tuple

# Tuple Immutability
# t7[0] = 10 # This will give an error because tuple is unchangeable

# Tuple Deletion
# del t7 # This will give an error because tuple is unchangeable

# Tuple Methods
print(t7.count(2)) # This will count the number of times 2 is present   
print(t7.index(4)) # This will give the index of the first occurrence of 4 in the tuple 

# Tuple with one element
t8 = (1,) # This is a tuple with one element, we need to add a comma after the element to make it a tuple
print(t8)

# Tuple without parentheses
t9 = 1, 2, 3 # This is also a tuple without parentheses
print(t9)

# Tuple with different data types
t10 = (1, "gaurav", 3.14, [1,2,3], {"name": "gaurav", "mobile": 8881438098})
print(t10)

# Tuple with nested tuples
t11 = (1, 2, (3, 4), (5, 6))
print(t11)

# Tuple with duplicate elements
t12 = (1, 2, 2, 3, 4, 4, 5)
print(t12)

# Tuple with mixed data types
t13 = (1, "gaurav", 3.14, [1,2,3], {"name": "gaurav", "mobile": 8881438098}, (1, 2), (3, 4), (5, 6), 1, 2, 2, 3, 4, 4, 5)
print(t13)

# Tuple with nested tuples and lists
t14 = (1, 2, (3, 4), [5, 6], (7, 8), [9, 10])
print(t14)

# Tuple with nested tuples and dictionaries
t15 = (1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, (5, 6), {"name": "gaurav", "mobile": 8881438098})
print(t15)

# Tuple with nested tuples, lists and dictionaries
t16 = (1, 2, (3, 4), [5, 6], {"name": "gaurav", "mobile": 8881438098}, (7, 8), [9, 10], {"name": "gaurav", "mobile": 8881438098})
print(t16)

# Tuple with nested tuples, lists, dictionaries and sets
t17 = (1, 2, (3, 4), [5, 6], {"name": "gaurav", "mobile": 8881438098}, (7, 8), [9, 10], {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3})
print(t17)

# Tuple with nested tuples, lists, dictionaries, sets and frozensets
t18 = (1, 2, (3, 4), [5, 6], {"name": "gaurav", "mobile": 8881438098}, (7, 8), [9, 10], {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}))
print(t18)

# Tuple with nested tuples, lists, dictionaries, sets, frozensets and booleans
t19 = (1, 2, (3, 4), [5, 6], {"name": "gaurav", "mobile": 8881438098}, (7, 8), [9, 10], {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False)
print(t19)

# Tuple with nested tuples, lists, dictionaries, sets, frozensets, booleans and None
t20 = (1, 2, (3, 4), [5, 6], {"name": "gaurav", "mobile": 8881438098}, (7, 8), [9, 10], {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None)
print(t20)

# Tuple with nested tuples, lists, dictionaries, sets, frozensets, booleans, None and complex numbers
t21 = (1, 2, (3, 4), [5, 6], {"name": "gaurav", "mobile": 8881438098}, (7, 8), [9, 10], {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2))
print(t21)

# Tuple with nested tuples, lists, dictionaries, sets, frozensets, booleans, None, complex numbers and bytes
t22 = (1, 2, (3, 4), [5, 6], {"name": "gaurav", "mobile": 8881438098}, (7, 8), [9, 10], {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), b'hello')
print(t22)

# Tuple with nested tuples, lists, dictionaries, sets, frozensets, booleans, None, complex numbers, bytes and bytearrays
t23 = (1, 2, (3, 4), [5, 6], {"name": "gaurav", "mobile": 8881438098}, (7, 8), [9, 10], {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), b'hello', bytearray(b'world'))
print(t23)

# Tuple with nested tuples, lists, dictionaries, sets, frozensets, booleans, None, complex numbers, bytes, bytearrays and memoryviews
t24 = (1, 2, (3, 4), [5, 6], {"name": "gaurav", "mobile": 8881438098}, (7, 8), [9, 10], {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), b'hello', bytearray(b'world'), memoryview(b'hello world'))
print(t24)

# Tuple with nested tuples, lists, dictionaries, sets, frozensets, booleans, None, complex numbers, bytes, bytearrays, memoryviews and range
t25 = (1, 2, (3, 4), [5, 6], {"name": "gaurav", "mobile": 8881438098}, (7, 8), [9, 10], {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), b'hello', bytearray(b'world'), memoryview(b'hello world'), range(1, 10))
print(t25)

# Tuple with nested tuples, lists, dictionaries, sets, frozensets, booleans, None, complex numbers, bytes, bytearrays, memoryviews, range and functions
def func():
    return "Hello World"

t26 = (1, 2, (3, 4), [5, 6], {"name": "gaurav", "mobile": 8881438098}, (7, 8), [9, 10], {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), b'hello', bytearray(b'world'), memoryview(b'hello world'), range(1, 10), func)
print(t26)

# Tuple with nested tuples, lists, dictionaries, sets, frozensets, booleans, None, complex numbers, bytes, bytearrays, memoryviews, range, functions and classes
class MyClass:
    def __init__(self, name):
        self.name = name

t27 = (1, 2, (3, 4), [5, 6], {"name": "gaurav", "mobile": 8881438098}, (7, 8), [9, 10], {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), b'hello', bytearray(b'world'), memoryview(b'hello world'), range(1, 10), func, MyClass)
print(t27)

# Tuple with nested tuples, lists, dictionaries, sets, frozensets, booleans, None, complex numbers, bytes, bytearrays, memoryviews, range, functions, classes and modules
import math
t28 = (1, 2, (3, 4), [5, 6], {"name": "gaurav", "mobile": 8881438098}, (7, 8), [9, 10], {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), b'hello', bytearray(b'world'), memoryview(b'hello world'), range(1, 10), func, MyClass, math)
print(t28)
