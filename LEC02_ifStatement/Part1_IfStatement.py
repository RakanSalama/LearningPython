if 5 > 2:
    print("YES! 5 is greater than 2")
    print("TEST")
if 2 > 1 :
    print("two is greater than one")


Name = "Rakan Salama" 
number = 5
if 1 == 1 :
    print(Name)
if 1 > 0 :
    print(number)

#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#a short way to make if statement
if a > b: print("a is greater than b")

#OR
print("A") if a > b else print("B")

#OR
print("A") if a > b else print("=") if a == b else print("B")

#We can use and & or in if statements
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
if a > b or a > c:
  print("At least one of the conditions is True")

#We can make nested loops (Nested = loop inside a loop :))
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#Pass , We use Pass to put an if statement and not get any error 
#for example, if you wanna make many if statments and want to type the content of that if
# you can put pass so it won't do anything
if x == 41:
  pass
