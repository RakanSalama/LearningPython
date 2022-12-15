thislist = ["apple", "banana", "cherry", "Hi"]
thislist.remove("banana") # to remove an item using item's name we use .remove()
thislist.pop(1) # if we want to remove an item using index we use .pop()
print(thislist)
thislist.pop() # only the last item will be removed
print(thislist)
#Del to remove an index or a full of list 
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
del thislist # the list will be deleted completely
#print(thislist) it will give an error ( not defined )
thislist = ["apple", "banana", "cherry"]
thislist.clear()# it will make it empty 
print(thislist)
"""
Just in short, the diff between del and clear that del removes it all !
but clear will not delete the list and it will only remove the items inside it
and make it empty.
"""