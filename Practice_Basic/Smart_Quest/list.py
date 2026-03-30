my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)   # [10, 2, 3]

# List Methods
my_list.append(4)  # This will add 4 to the end of the list
print(my_list)   # [10, 2, 3, 4]
my_list.insert(1, 20)  # This will insert 20 at index 1
print(my_list)   # [10, 20, 2, 3, 4]
my_list.remove(2)  # This will remove the first occurrence of 2 from the list
print(my_list)   # [10, 20, 3, 4]
my_list.pop()  # This will remove the last element from the list
print(my_list)   # [10, 20, 3]
my_list.pop(1)  # This will remove the element at index 1 from the list
print(my_list)   # [10, 3]
my_list.clear()  # This will remove all elements from the list
print(my_list)   # []


# List Slicing
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # This will give a new list with elements from index 1 to 3
print(my_list[:3])  # This will give a new list with elements from index 0 to 2
print(my_list[3:])  # This will give a new list with elements from index 3 to the end

# List Comprehension
squared = [x**2 for x in my_list]   # This will create a new list with the squares of the elements in my_list
print(squared)   # [1, 4, 9, 16, 25]
even_numbers = [x for x in my_list if x % 2 == 0]  # This will create a new list with the even numbers from my_list
print(even_numbers)   # [2, 4]

# Nested List
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list)   # [[1, 2], [3, 4], [5, 6]]
print(nested_list[0])  # [1, 2]
print(nested_list[0][0])  # 1
print(nested_list[0][1])  # 2
print(nested_list[1])  # [3, 4]
print(nested_list[1][0])  # 3
print(nested_list[1][1])  # 4
print(nested_list[2])  # [5, 6]
print(nested_list[2][0])  # 5
print(nested_list[2][1])  # 6

# List Functions
print(len(my_list))  # This will give the length of the list
print(max(my_list))  # This will give the maximum element in the list
print(min(my_list))  # This will give the minimum element in the list
print(sum(my_list))  # This will give the sum of the elements in the list
print(sorted(my_list))  # This will give a new list with the elements of my_list sorted in ascending order
print(sorted(my_list, reverse=True))  # This will give a new list with the elements of my_list sorted in descending order

# List Membership
print(3 in my_list)  # This will return True if 3 is present in the list, otherwise False
print(6 in my_list)  # This will return False because 6 is not present in the list

# List Immutability
# my_list[0] = 10  # This will not give an error because list is mutable, but it will change the value at index 0 to 10
print(my_list)   # [10, 2, 3, 4, 5]

# List Copying
my_list_copy = my_list.copy()  # This will create a shallow copy of the list
print(my_list_copy)  # [10, 2, 3, 4, 5]
my_list_copy[0] = 20  # This will change the value at index 0 to 20 in the copied list
print(my_list_copy)  # [20, 2, 3, 4, 5]
print(my_list)  # [10, 2, 3, 4, 5]  # The original list remains unchanged

# List Deletion
del my_list[0]  # This will delete the element at index 0 from the list
print(my_list)  # [2, 3, 4, 5]
del my_list  # This will delete the entire list
# print(my_list)  # This will give an error because the list has been deleted

# List with one element
single_element_list = [1]  # This is a list with one element
print(single_element_list)  # [1]

# List with different data types
mixed_list = [1, "gaurav", 3.14, [1, 2, 3], {"name": "gaurav", "mobile": 8881438098}]
print(mixed_list)  # [1, 'gaurav', 3.14, [1, 2, 3], {'name': 'gaurav', 'mobile': 8881438098}]

# List with nested lists
nested_list = [1, 2, [3, 4], [5, 6]]
print(nested_list)  # [1, 2, [3, 4], [5, 6]]

# List with duplicate elements
duplicate_list = [1, 2, 2, 3, 4, 4, 5]
print(duplicate_list)  # [1, 2, 2, 3, 4, 4, 5]

# List with mixed data types
mixed_list = [1, "gaurav", 3.14, [1, 2, 3], {"name": "gaurav", "mobile": 8881438098}, [1, 2], [3, 4], [5, 6], 1, 2, 2, 3, 4, 4, 5]
print(mixed_list)  # [1, 'gaurav', 3.14 , [1, 2, 3], {'name': 'gaurav', 'mobile': 8881438098}, [1, 2], [3, 4], [5, 6], 1, 2, 2, 3, 4, 4, 5]

# List with nested lists and tuples
nested_list_tuple = [1, 2, (3, 4), [5, 6]]
print(nested_list_tuple)  # [1, 2, (3, 4), [5, 6]]

# List with nested lists and dictionaries
nested_list_dict = [1, 2, {"name": "gaurav", "mobile": 8881438098}, [5, 6]]
print(nested_list_dict)  # [1, 2, {'name': 'gaurav', 'mobile': 8881438098}, [5, 6]]

# List with nested lists, tuples and dictionaries
nested_list_tuple_dict = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}]
print(nested_list_tuple_dict)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}]

# List with nested lists, tuples, dictionaries and sets
nested_list_tuple_dict_set = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}]
print(nested_list_tuple_dict_set)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}]

# List with nested lists, tuples, dictionaries, sets and frozensets
nested_list_tuple_dict_set_frozenset = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6})]
print(nested_list_tuple_dict_set_frozenset)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6})]

# List with nested lists, tuples, dictionaries, sets, frozensets and booleans
nested_list_tuple_dict_set_frozenset_bool = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False]
print(nested_list_tuple_dict_set_frozenset_bool)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False]

# List with nested lists, tuples, dictionaries, sets, frozensets, booleans and None
nested_list_tuple_dict_set_frozenset_bool_none = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None]
print(nested_list_tuple_dict_set_frozenset_bool_none)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None]

# List with nested lists, tuples, dictionaries, sets, frozensets, booleans, None and complex numbers
nested_list_tuple_dict_set_frozenset_bool_none_complex = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2)]
print(nested_list_tuple_dict_set_frozenset_bool_none_complex)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, 1+2j]

# List with nested lists, tuples, dictionaries, sets, frozensets, booleans, None, complex numbers and functions
def my_function():
    return "Hello, World!"

nested_list_tuple_dict_set_frozenset_bool_none_complex_function = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), my_function]
print(nested_list_tuple_dict_set_frozenset_bool_none_complex_function)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, 1+2j, <function my_function at 0x7f8c8c8c8c8c>]

# List with nested lists, tuples, dictionaries, sets, frozensets, booleans, None, complex numbers, functions and classes
class MyClass:
    def __init__(self, name):
        self.name = name
nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), my_function, MyClass]
print(nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class)  #[1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, 1+2j, <function my_function at 0x7f8c8c8c8c8c>, <class '__main__.MyClass'>]

# List with nested lists, tuples, dictionaries, sets, frozensets, booleans, None, complex numbers, functions, classes and modules
import math
nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), my_function, MyClass, math]
print(nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, 1+2j, <function my_function at 0x7f8c8c8c8c8c>, <class '__main__.MyClass'>, <module 'math' (built-in)>]

# List with nested lists, tuples, dictionaries, sets, frozensets, booleans, None, complex numbers, functions, classes, modules and other lists
nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), my_function, MyClass, math, [1, 2, 3]]
print(nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, 1+2j, <function my_function at 0x7f8c8c8c8c8c>, <class '__main__.MyClass'>, <module 'math' (built-in)>, [1, 2, 3]]

# List with nested lists, tuples, dictionaries, sets, frozensets, booleans, None, complex numbers, functions, classes, modules and other lists
nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), my_function, MyClass, math, [1, 2, 3], [[1, 2], [3, 4]]]
print(nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, 1+2j, <function my_function at 0x7f8c8c8c8c8c>, <class '__main__.MyClass'>, <module 'math' (built-in)>, [1, 2, 3], [[1, 2], [3, 4]]]

# List with nested lists, tuples, dictionaries, sets, frozensets, booleans, None, complex numbers, functions, classes, modules and other lists, tuples
nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list_tuple = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), my_function, MyClass, math, [1, 2, 3], [[1, 2], [3, 4]], (5, 6)]
print(nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list_tuple)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, 1+2j, <function my_function at 0x7f8c8c8c8c8c>, <class '__main__.MyClass'>, <module 'math' (built-in)>, [1, 2, 3], [[1, 2], [3, 4]], (5, 6)]

# List with nested lists, tuples, dictionaries, sets, frozensets, booleans, None, complex numbers, functions, classes, modules and other lists, tuples and dictionaries
nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list_tuple_dict = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), my_function, MyClass, math, [1, 2, 3], [[1, 2], [3, 4]], (5, 6), {"name": "gaurav", "mobile": 8881438098}]
print(nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list_tuple_dict)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, 1+2j, <function my_function at 0x7f8c8c8c8c8c>, <class '__main__.MyClass'>, <module 'math' (built-in)>, [1, 2, 3], [[1, 2], [3, 4]], (5, 6), {'name': 'gaurav', 'mobile': 8881438098}]


# List with nested lists, tuples, dictionaries, sets, frozensets, booleans, None, complex numbers, functions, classes, modules and other lists, tuples, dictionaries and sets
nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list_tuple_dict_set = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), my_function, MyClass, math, [1, 2, 3], [[1, 2], [3, 4]], (5, 6), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}]
print(nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list_tuple_dict_set)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, 1+2j, <function my_function at 0x7f8c8c8c8c8c>, <class '__main__.MyClass'>, <module 'math' (built-in)>, [1, 2, 3], [[1, 2], [3, 4]], (5, 6), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}]

# List with nested lists, tuples, dictionaries, sets, frozensets, booleans, None, complex numbers, functions, classes, modules and other lists, tuples, dictionaries, sets and frozensets
nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list_tuple_dict_set_frozenset = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), my_function, MyClass, math, [1, 2, 3], [[1, 2], [3, 4]], (5, 6), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6})]
print(nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list_tuple_dict_set_frozenset)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, 1+2j, <function my_function at 0x7f8c8c8c8c8c>, <class '__main__.MyClass'>, <module 'math' (built-in)>, [1, 2, 3], [[1, 2], [3, 4]], (5, 6), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6})]


# List with nested lists, tuples, dictionaries, sets, frozensets, booleans, None, complex numbers, functions, classes, modules and other lists, tuples, dictionaries, sets, frozensets and booleans
nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list_tuple_dict_set_frozenset_bool = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), my_function, MyClass, math, [1, 2, 3], [[1, 2], [3, 4]], (5, 6), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True]
print(nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list_tuple_dict_set_frozenset_bool)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, 1+2j, <function my_function at 0x7f8c8c8c8c8c>, <class '__main__.MyClass'>, <module 'math' (built-in)>, [1, 2, 3], [[1, 2], [3, 4]], (5, 6), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True]

# List with nested lists, tuples, dictionaries, sets, frozensets, booleans, None, complex numbers, functions, classes, modules and other lists, tuples, dictionaries, sets, frozensets, booleans and None
nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list_tuple_dict_set_frozenset_bool_none = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), my_function, MyClass, math, [1, 2, 3], [[1, 2], [3, 4]], (5, 6), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, None]
print(nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list_tuple_dict_set_frozenset_bool_none)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, 1+2j, <function my_function at 0x7f8c8c8c8c8c>, <class '__main__.MyClass'>, <module 'math' (built-in)>, [1, 2, 3], [[1, 2], [3, 4]], (5, 6), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, None]

# List with nested lists, tuples, dictionaries, sets, frozensets, booleans, None, complex numbers, functions, classes, modules and other lists, tuples, dictionaries, sets, frozensets, booleans, None and complex numbers
nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list_tuple_dict_set_frozenset_bool_none_complex = [1, 2, (3, 4), {"name": "gaurav", "mobile": 8881438098}, [5, 6], (7, 8), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, complex(1, 2), my_function, MyClass, math, [1, 2, 3], [[1, 2], [3, 4]], (5, 6), {"name": "gaurav", "mobile": 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, None, complex(1, 2)]
print(nested_list_tuple_dict_set_frozenset_bool_none_complex_function_class_module_list_list_tuple_dict_set_frozenset_bool_none_complex)  # [1, 2, (3, 4), {'name': 'gaurav', 'mobile': 8881438098}, [5, 6], (7, 8), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, False, None, 1+2j, <function my_function at 0x7f8c8c8c8c8c>, <class '__main__.MyClass'>, <module 'math' (built-in)>, [1, 2, 3], [[1, 2], [3, 4]], (5, 6), {'name': 'gaurav', 'mobile': 8881438098}, {1, 2, 3}, frozenset({4, 5, 6}), True, None, 1+2j]

