# We can insert an item by using .insert() other items will be pushed +1
thislist = ["apple", "banana", "cherry"]
thislist.insert(1,"InsertedItem")
print(thislist)
# We can extend a list by doing .extend()
thislist = ["apple", "banana", "cherry"]
names = ["Rakan","Rayan"] # we can make it as ("Rakan","Rayan") it doesn't only extend lists
thislist.extend(names)
print(thislist) # this list will contain names list ^^\