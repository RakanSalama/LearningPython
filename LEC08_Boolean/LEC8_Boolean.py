print(1>2)
print(1==1)

num1 = 1 
num2 = 2
print("------------------------------")
if num2 > num1:
    print("num2 is greater than num1")
else:
    print("num1 is greater than num2")

print("------------------------------")
print(bool("Hello")) # if a string had nothing it will print false
print(bool(""))
print("---------")
print(bool(15)) # if the number was 0 it will print false 
print(bool(0))
print("---------")
print(bool(["apple", "cherry", "banana"])) # if it was empty it will print false 
print(bool([]))
print("------------------------------")
# False values 
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print("------------------------------")
# Using class and methods 
class myclass():
  def __len__(self):
    return 0

myobj = myclass() # it will bring 0 
print(bool(myobj))
print("-------------")

def myFunction() :
  return True

print(myFunction())
print("-------------")

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
print("------------------------------")
#Check if x is int or no 
x = 200
print(isinstance(x, int))
print(isinstance(x, str))
