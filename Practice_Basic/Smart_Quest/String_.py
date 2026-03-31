a = "Hello, World!"
print("a.upper():", a.upper())
print("a.lower():", a.lower())
print("a.capitalize():", a.capitalize())
print("a.title():", a.title())
print("a.swapcase():", a.swapcase())
print("a.count('o'):", a.count("o"))
print("a.find('o'):", a.find("o"))
print("a.replace('o', '0'):", a.replace("o", "0"))
print("a.split(','):", a.split(","))
print("a.strip('!'):", a.strip("!"))
print("a.startswith('Hello'):", a.startswith("Hello"))
print("a.endswith('!'):", a.endswith("!"))


a = "Hello"
b = "World"
c = a + b
print(c)
d = a * 3
print(d)


age = 36
txt = f"My name is John, I am {age}"
print(txt)
name = "John"
age = 36
txt = "My name is {}, I am {}".format(name, age)
print(txt)

price = 59
txt = f"The price is {price:.3f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)


x = ["apple", "banana"]
print("banana" in x)

y = "Hello, World!"
print("World" in y)

x = ["apple", "banana"]
print("pineapple" not in x)


# #######################################################################################
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
# #######################################################################################


# #######################################################################################
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
print(x is not y)
print(x != y)
# #######################################################################################
