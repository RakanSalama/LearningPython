# we only type .pop() to delete an item or del() or clear()

#way one - with paramters inside it 
dict = {"Name" : "Rakan", "Age": 22}
dict.pop("Name")
print(dict)
#way one + item - without parameters ( it will only delete the last inserted item )
dict = {"Name" : "Rakan", "Age": 22}
dict.popitem()
print(dict)

#way two - with parameters inside it 

dict = {"Name" : "Rakan", "Age": 22}
del dict["Name"]
print(dict)

#way two - without parameters ( it will delete all the dictionary )


dict = {"Name" : "Rakan", "Age": 22}
del dict
print(dict)

#way three

dict = {"Name" : "Rakan", "Age": 22}
dict.clear()
print(dict)