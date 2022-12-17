"""
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
"""
tup = ("Rakan","Rayan","Remah")
lis = list(tup)

#replace rakan to ahmed
lis[0] = "Ahmed"
tup = tuple(lis)
print(tup)

#add item
lis.append("Khalid")
tup = tuple(lis)
print(tup)
# or make a new tuple and add it to the prev tuple
tup = ("Rakan","Rayan","Remah")
tup2 = ("Marwan",)
tup = tup + tup2
print(tup) 

# we can't remove items in a tuple, we need to convert it to list then return it to a tuple
tup = ("Rakan","Rayan","Remah")
tup1 = list(tup)
tup1.remove("Rakan")
tup = tuple(tup1)
print(tup)

# How to delete a tuple Completly?
del tup
#print(tup) it will give us :NameError: name 'tup' is not defined. Did you mean: 'tup2'?



