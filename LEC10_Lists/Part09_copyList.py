# if we copy a list by using this method we will face a problem
# the list will refrence to list1 and if we change in list 2 
# we will change in list1 :(
list1 = ["Rakan","Rayan"]
list2 = list1
list2.append("Bander")
print(list2)
print(list1)
print("----------------------------")
#To avoid this problem we need to use .copy() function
list3 = ["jeddah","Makkah"]
list4 = list3.copy()
list4.append("AlBaha")
print(list4)
print(list3)
