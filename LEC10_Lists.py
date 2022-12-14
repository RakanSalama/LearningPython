
# print a list 
list = ["Rakan", "Rayan" , "Remah"]
print(list)
# How to know the length of the list ?
print("The size of the list is:", len(list))
# we can put anytype of data in the list , These are exampls of some diffrent kind of lists str,int,boolean
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False] 
# We can mix them in one list like this example:
list1 = ["abc", 34, True, 40, "male"]
# Also we can know if the var is a list or not by using type()
print(type(list1)) # it will be type <list>

"""
We can define a list using list()
as we know, we use x = [1,2,3,4] OR x = list((1,2,3,4))

x = list(("Rakan","Rayan","Remah"))
print(x)
"""

"""
List -> is a collection which is ordered and changeable. Allows duplicate members.                               Duplicated = 1,1,2,2,3,3 etc.. 
Tuple-> is a collection which is ordered and unchangeable. Allows duplicate members.
Set  -> is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary -> is a collection which is ordered** and changeable. No duplicate members.
"""
print("-----------------ACCESS LIST ITEMS-----------------")
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
print("-----------------Change Items Values-----------------")
list = ["Rakan","Rayan","Remah","Khalid"]
list[1] = "Ahmed"
print(list)
#Here we will change 2 items (3rd + 4th)
list[2:4]= ["Hamad","Sara"]
print(list)
#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# another exception :
thislist = ["apple", "banana", "cherry","Hi"]
thislist[1:3] = ["watermelon"] # cherry will be removed :(
print(thislist)

print("-----------------Insert Items-----------------")
# We can insert an item by using .insert() other items will be pushed +1
thislist = ["apple", "banana", "cherry"]
thislist.insert(1,"InsertedItem")
print(thislist)
# We can extend a list by doing .extend()
thislist = ["apple", "banana", "cherry"]
names = ["Rakan","Rayan"] # we can make it as ("Rakan","Rayan") it doesn't only extend lists
thislist.extend(names)
print(thislist) # this list will contain names list ^^\
print("-----------------Remove Items-----------------")
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
print("-----------------Loop & list-----------------")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# or we can make it like this 
thislist = ["R", "A", "K"]
for x in range(len(thislist)):
    print(thislist[x])
print("-------")
# or like in java style using while :)
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
print("-------")
# The shortest way to make a loop that print these items is:
[print(x) for x in thislist]
print("-----------------List Comprehension-----------------")
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









