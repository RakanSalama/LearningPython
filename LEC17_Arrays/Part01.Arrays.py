# Python doesn't have arrays, but we use lists as arrays ^^
Names = ["Rakan","Rayan","Remah"]

FirstName = Names[0]
print("First Name in the list is",FirstName)
Names[1] = "Ahmed"
print("Rayan got changed to",Names[1])

#To know the length of the list:
print(len(Names))

print("The item of the list is: ")
#Loops and list 
for x in Names:
    print(x)

#if we want to add a new item in the list we can do it like that:
Names.append("Hello i am extra:)")
print(Names)

#To remove items in the list:
Names.pop() # it will remove the last item 
print(Names)

Names.pop(1) # it will remove the second item 
print(Names)

#To remove a specific use .remove
Names.remove("Remah")
print(Names)

#Methods for lists :)
"""

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""