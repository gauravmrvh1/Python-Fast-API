# Sets are used to store multiple items in a single variable.

thisSet = {"apple", "banana", "cherry"}
print(thisSet)

# Accessing Items
# You cannot access items in a set by referring to an index or a key, since sets are unordered, unchangeable, and do not allow duplicate values.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# Loop through the set, and print the values:
for x in thisSet:
    print(x)

# Check if "banana" is present in the set:
print("banana" in thisSet)

# Adding Items
# To add one item to a set use the add() method.
thisSet.add("orange")
print(thisSet)

# To add more than one item to a set use the update() method.
thisSet.update(["orange", "mango", "grapes"])
print(thisSet)

# Removing Items
# To remove an item in a set, use the remove(), or the discard() method.
# The remove() method will raise an error if the specified item does not exist, and the discard() method will not raise an error if the specified item does not exist.
thisSet.remove("banana")
print(thisSet)

thisSet.discard("banana")
print(thisSet)

# You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
thisSet.pop()
print(thisSet)

# The clear() method empties the set:
thisSet.clear()
print(thisSet)

# The del keyword will delete the set completely:
del thisSet
# print(thisSet) # this will raise an error because the set no longer exists



set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)



set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
mySet = set1.union(set2, set3, set4)
print(mySet)

mySet = set1 | set2 | set3 | set4
print(mySet)


x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)


print("************************************************")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set1)
print(set2)
print(set3)

set1 = {"apple", "banana", "cherry"
        }
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)
print(set2)


set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", "microsoft", "apple", True}
set3 = set1.intersection(set2)
print(set3)



set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

set3 = set1 - set2
print(set3)