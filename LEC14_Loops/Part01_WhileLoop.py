# An example of a while loop
i = 1 
while i < 6:
    print("Number:",i)
    i = i + 1
print("----------------------------")
#We can add an else after the while so it make that command after it finishes from while loop
i = 1 
while i < 6:
    print("Number:",i)
    i = i + 1
else:
    print("Done")
print("----------------------------")
# if we wanna stop the loop in a certin point while the loop isn't finished 

i = 1 
while i < 6:
    print("Number:",i)
    i = i + 1
    if i == 3:
        break
else:
    print("Done")
print("----------------------------")
# if we want the loop to skip all the next code in the while and return back we can use continue
i = 1 
while i < 6:
    i = i + 1
    if i == 3:
        continue
    print("Number:",i)
else:
    print("Done")

#if we put break it won't do else if it got breaked 
i = 1 
while i < 6:
    i = i + 1
    if i == 3:
        break
    print("Number:",i)
else:
    print("Done")