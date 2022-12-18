set = {"Rakan", "Rayan", "Remah"}
print(set)
#List = [] brackets
#Tuple= () Parentheses
#Set  = {} curly Parentheses
"""
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

we can't make duplicated items like:
thisset = {"apple", "banana", "cherry", "apple"}

"""
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#Get the length (same as list and tuples)
print(len(thisset))
#Types that we can put inside the set ( same as list and tuples )
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4= {"abc", 34, True, 40, "male"}
#Same way to know the type of the list (using type)
print(type(set1))
# we can make anything to constructor 
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
