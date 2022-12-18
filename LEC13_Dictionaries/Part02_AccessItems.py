dict = {"Name" : "Rakan", "Age": 22}
print(dict["Name"]) 
# as we saw, it's like accessing a list or a tuple but you should put the name of the key
#Another way to get access to anyitem you want in the dict
print(dict.get("Age"))

#To know the keys of the dictionary
print(dict.keys())
#To know the values of the keys
print(dict.values())
#it will return the value and the key as tuples 
print(dict.items())

#To know if this item is in the dict or not. (Note : it only work for keys not values)
if "Name" in dict:
    print("Name is in the items of the dictionary")
    