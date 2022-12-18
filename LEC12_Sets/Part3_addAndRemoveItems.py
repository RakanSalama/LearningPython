# as we said before, we can't replace or change items, but we only can add or remove
set1= {"Rakan","Rayan","Remah"}
set1.add("Ahmed")
print(set1)

#we can add other set's items to the main set by using .update()
set2={"Test"}
set1.update(set2)
print(set1)

#we can add a list or tuple to the set by using .update()
list1= ["Khalid"]
set1.update(list1)
print(set1)


#Remove items by using ( remove(), discard(), pop(), del)

# The diffrence between remove() and discard()
# remove() = gives an error if this item isn't found
# discard()= doesn't give an error 

#Remove
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#thisset.remove("banana") it will give us error

#discard
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
thisset.discard("banana") # it will not do anything and it will not give an error

#Using pop(), Note: it will remove random item 
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# We use clear to remove all items without remove the set itself 

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#using Del
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)