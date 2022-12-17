list1 = ["a","b"]
list2 = [3,4]
list3 = list1  + list2
# it will not support list3.sort() because it's mixed 
print(list3)
# Another way to append two lists one by one
list4= []
for x in list2:
    list1.append(x)
print(list1)
# another easy way to add two lists by using .extend()
list5 = [1,2]
list6 = ["a","b"]
list5.extend(list6)

