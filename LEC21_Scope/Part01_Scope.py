#What is scope ?
#A variable is only available from inside the region it is created. This is called scope.

def myfunc():
  x = 300
  print(x)
myfunc()

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
#print(x) x is only defined inside the function :(
print("------------------")
x = 300

def myfunc():
  print(x)

myfunc()

print(x) # x is defined outside the function
print("------------------")
#Tricky example
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#Global word
def myfunc():
  global x
  x = 300

myfunc()

print(x)
print("------------------")
#Tricky global example:
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

#In short. Scope is the place that x that will be defined and included ^^ 