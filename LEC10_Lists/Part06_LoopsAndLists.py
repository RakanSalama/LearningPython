thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# or we can make it like this 
thislist = ["R", "A", "K"]
for x in range(len(thislist)):
    print(thislist[x])
print("-------")
# or like in java style using while :)
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
print("-------")
# The shortest way to make a loop that print these items is:
[print(x) for x in thislist]