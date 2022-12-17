#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
# which means we take the values and put them in variables
fruits = ("apple", "banana", "cherry") # Packing

(green, yellow, red) = fruits # unPacking

print(green)
print(yellow)
print(red)

#What if the values inside the tuple were more than the variables that we cant to unpack?
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) # all the rest values will go to it 

print("-------------------------------")
#What if we want to give the middle unpacked value the rest and the last item only for red?

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic) # it will not contain the last item 
print(red) # it will only take the last item 
