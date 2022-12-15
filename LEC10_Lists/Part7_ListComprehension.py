# If the item has the letter A it will be added in the newList :)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

print("-------")
# same way but shorter :)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# If the item was apple it will not be added in the list
newlist = [x for x in fruits if x != "apple"]
print(newlist)
#if we want to add only 3 items only :
newlist = [x for x in range(3)]
print(newlist)
# if we want to make all the items in uppercase 
newlist = [x.upper() for x in fruits]
print(newlist)
# if we want to make all the values to hello :
newlist = ['hello' for x in fruits]
print(newlist)
# if we want to change an item that we read into something else
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)# if it see banana it will change it to orange :)
