print("____________________[Print diffrent var types]___________________")
Number = 10
Name = "Rakan Salama"
print(Number)
print(Name)
print("____________________[OverWriting]___________________")
x = 5
x = 2                         # 2 will overwrite 5
print(x)
a = 1
A = 2                         # A will not overwrite a because they are diffrent
print(A)
print(a)
print("____________________[Print type]___________________")
Change_Var= str(3)  # it will be '3'
print(Change_Var)
Change_Var= int(3)  # it will be 3
print(Change_Var)
Change_Var= float(3)# it will be 3.0
print(Change_Var)
print("____________________[Show var type]___________________")
x = 10
y = "10"                          # To know the data of variable
print(type(x))
print(type(y))
print("____________________[String type]___________________")
String_name1 = "Rakan"
print(String_name1)
String_name2 = 'Rakan'            # They are the same
print(String_name2)
print("____________________[Valid var and invalid var]___________________")
# valid names that you can make
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"                                
MYVAR = "John"
myvar2 = "John"
# Invalid names that you can't make
"""
2myvar = "John"
my-var = "John"            # you can't make like these names
my var = "John"
"""
print("____________________[multi var]___________________")
x = y = z = "We have the same value"
print(x)
print(y)
print(z)

names = ["Rakan","Rayan","Remah"]
x, y, z = names
print(x)
print(y)
print(z)
print("____________________[One print that has many var]___________________")
x = "HELLO WORLD ^^"
print(x)

x = "Rakan"
y = "Rayan"
z = "Remah"
f = 5
h = 1
print(x,y,z,5) # it makes space and we can add diffrent types
print(f + h)
print(x + z + y) # it doesn't make any space and they must be same type
# if we did print(x + z + y + f) it will give us an error because f is diffrent type
print("____________________[Global variables]___________________")
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


