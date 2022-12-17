#Access a tuple is like accessing arrays. Here are some exampels:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])
#Loop to know if this item is inside the tuple or not
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")