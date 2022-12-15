global_var = "Fun"
def FirstFunction():
    print("Python is " + global_var)
def SecondFunction():
    print("Rakan had " + global_var)

FirstFunction()
SecondFunction()

print("---------------------------")

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)       # x is global and it will not be overwritten if we defined
                                # x inside a function, x will be changed only inside this function
myfunc()

print("Python is " + x)
print("---------------------------")
def myFunctionV2():
    global x 
    x = "OKAY"
myFunctionV2()
print("Rakan is " + x)
print("---------------------------")
x = "nice"
def myFunctionV2():
    global x 
    x = "OKAY"
myFunctionV2()
print("Rakan is" + x)