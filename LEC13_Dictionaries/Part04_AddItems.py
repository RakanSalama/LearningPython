# We can add items by making a new "key" and give it a value same as
# changing the values 
#way one
dict = {"Name" : "Rakan", "Age": 22}
dict["Lives in"] = "Jeddah"
print(dict)
#way two
dict.update({"Brother's name": "Rayan"})
print(dict)

