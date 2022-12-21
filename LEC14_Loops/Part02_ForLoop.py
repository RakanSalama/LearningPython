Names = ["Rakan","Rayan","Remah"]
for x in Names:
    print(x)
print("----------------")
for x in "Rakan":
    print(x)
print("----------------")
#we can use break inside for loop like:
for x in Names:
    print(x)
    if x == "Rakan":
        break
print("----------------")
#Also we can use continue in for loops like:
for x in Names:
    if x == "Rakan":
        continue
    print(x)
print("----------------")
#Using range()
for x in range(5): # it will start from 0
    print(x)
print("----------------")
for x in range(2, 6): #range(start,end)
  print(x)
print("----------------")
for x in range(2, 30, 3): #range(start,end,sequence number 3 6 9 etc..)
  print(x)
print("----------------")
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#if we put break, it won't do else statement
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Nested loop example
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#We can use pass in loops too ^^!
for x in Names:
    pass
