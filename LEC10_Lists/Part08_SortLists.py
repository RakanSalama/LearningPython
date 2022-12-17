# Sorting Strings * a b c d e f g ... *
List1 = ["z","x","b","a"]
List1.sort()
print(List1)
# Sorting Numbers
List2 = [1 , 6 , 5 , 2 , 100]
List2.sort()
print(List2)
# Desending "Reverse"
List1.sort(reverse= True)
List2.sort(reverse= True)

print(List1)
print(List2)
# Customize a sort function (ex: numbers near 50)
def SortCustomize(n):
    return abs(n - 50)
list3 = [5,1,2,7,10,68]
list3.sort(key = SortCustomize)
print(list3)
#You should know that capital letters being sorted before lower letters
#for example:
list4 = ["Rakan","Ahmed","rakan","ahmed"]
list4.sort()
print(list4)
# WE can make the sorting ignore the uppercase if there was a lowercase before it"like a" ( we need to implement a key)
list4.sort(key = str.lower)
print(list4) # it will print Ahmed , ahmed , Rakan , rakan
# There is a reverse function
list5 = [1,2,3,4,5,6,10]
list5.reverse()
print(list5)
# we can reverse any list by using 
# list.reverse() 
# or 
# list.sort(reverse = True)

