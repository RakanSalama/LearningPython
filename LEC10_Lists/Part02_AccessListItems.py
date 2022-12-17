thislist = ["Rakan", "banana", "cherry"]
print(thislist[0]) # first item
print(thislist[-1]) # last item 
# lets say we want to print only the 1-2 items only and ignore the first one how?
print(thislist[1:3])
# How about if we want to print the first 2 items in the list?
print(thislist[:2])
# How about if we want to start printing from the second item ?
print(thislist[1:])
#How about if we want to print from the last 4 items without the last item ?
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# An example of how to check if this item is in the list or not
list = ["Rakan","Rayan","Remah"]
if "Rayan" in list:
    print("Rayan is in the list")