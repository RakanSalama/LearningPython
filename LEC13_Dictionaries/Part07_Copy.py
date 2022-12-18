# We can't do dict1 = dict2 because if we changed anything in dict2 or dict1 it will be implemeneted in the other one

dict1 = {"Name" : "Rakan", "Age": 22}
dict2 = dict1.copy()
print(dict2)

#or

dict3 = {"Name" : "Rakan", "Age": 22}
dict4 = dict(dict3)
print(dict4)