list = ["Rakan","Rayan","Remah","Khalid"]
list[1] = "Ahmed"
print(list)
#Here we will change 2 items (3rd + 4th)
list[2:4]= ["Hamad","Sara"]
print(list)
#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# another exception :
thislist = ["apple", "banana", "cherry","Hi"]
thislist[1:3] = ["watermelon"] # cherry will be removed :(
print(thislist)
