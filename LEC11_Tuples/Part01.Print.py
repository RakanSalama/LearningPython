thistuple = ("banana", "apple", "cherry")
print(thistuple)
"""
First, you must know that
list = []
tuple = ()

Tuple items are ordered, unchangeable, and allow duplicate values.
Ordered:
When we say that tuples are ordered, it means that the items have a defined
order, and that order will not change.
Unchangeable:
Tuples are unchangeable, meaning that we cannot change, add or remove 
items after the tuple has been created.

thistuple[0] = "x"    We can't do this in tuples
print(thistuple)

Duplicated items : 
It allow duplicated items like: 
thistuple = ("apple", "banana", "cherry", "apple", "cherry")

"""
#Tuple length ( like lists )
print("The length of this tuple is:",len(thistuple))

#You can't create a tuple with only one item like lists. 
Tup = ("Rakan")
print(type(Tup))
Tup = ("Rakan","Rayan")   # It will only know if this item is a tuple if it had many items, otherthan that it will count it as a str
print(type(Tup))          # except if you type tuple("Hello") it will give type tuple even if it was one item

#Tuple data typles(like lists)
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

#The tuple() Constructor 
tup = tuple("Hello")
print(type(tup))


# Sorting 
#print(thistuple.sort())  We can't do that 
# to sort a tuple we can do it only in this way: 
tuple_ = ('Itika', 'Arshia', 'Peter', 'Parker')  
print(tuple(sorted(tuple_)))
