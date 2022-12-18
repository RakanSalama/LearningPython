dict = {"Name" : "Rakan", "Age": 22}
for x in dict: # it will only print the keys 
    print(x)

for x in dict: # it will print the values of these keys
    print(dict[x])
#or 
for x in dict.values():
    print(x)

# if you want to print both by using .items()
for x,y in dict.items():
    print(x, y)
