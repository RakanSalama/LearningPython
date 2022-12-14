x = 2
y = 4
#-----------------------------
#Addition 
print("x + y =", x + y)
#Subtraction 
print("x - y =", x - y)
#Multiplication 
print("x * y =", x * y)
#Division
print("x / y =", x / y)
#Modulus
print("x % y =", x % y)
#Exponentiation
print("x ** y (2^4)=", x ** y)
#Floor division
print("x // y =", x // y)
print("---------------------------------------")
print("Read the comments for shortcut operations")
#We can use these in operations: 
"""
we can make a short cut to make it less to read.
instead of writing x = x + 1 -> x+= 1
and we can use it in other operators like / * etc.. 
"""
print("---------------------------------------")
print("Read the comments for operatros comparison")
"""
We can use these operators to do comparison:
== -> Equal
!= -> not equal
>  -> Greater than
<  -> Less than
>= -> Greater than or equal to 
<= -> Less than or equal to
"""
print("---------------------------------------")
# Logical operatros , note : It's unlike java, you must write " and "
no1 = 1
no2 = 2
if no1 == 1 and no2 == 2:
    print("Both are correct")
if no1 == 1 or no2 == 3:
    print("One of them is correct ")
if not(no1 == 3 and no2 == 4):
    print("None of them is correct")
print("---------------------------------------")
# using is, and is not 
print(no1 is no2) # we can say it's like no1 == no2
print(no1 is not no2) # we can say it's like no1!= no2

# Using in, or not in
x = ["apple", "banana"]
print("banana" in x)





