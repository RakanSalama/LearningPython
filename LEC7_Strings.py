print("UwU")
print('UwU')  # We can use one of them, it doesn't matter
print("------------------")
name = "Rakan"
print(name)
print("------------------")

x = """Hello my name is rakan and i love cats ^^
i am a student in FCIT and i am looking to improve my self 
wish me luck:)"""
print(x)
print("------------------")
MyName = "Rakan Salama"
print(MyName[0])   # we can print only 1 char of the string :)

print("------------------")
#Loop that prints each char of the string 
for x in "Hello":
    print(x)
print("------------------")
#Print the length of a String 
X = "ABCDEFG"
print(len(X))
print("------------------")
# Check if the text have a wanted String in it (using if statement)
text = "Hello my name is Rakan"
if "Rakan" in text:
    print("There is rakan in the wanted text")

if "Cats" not in text:
    print("There is NO CATS!!!!!")
print("------------------")
#Check if there is the wanted text or not (by giving true or false)
checkText = "i love cats because they are cats :)"
print("Oh no, cats again..." not in checkText)
print("----------------------------------------------------------------------------")
# Slice the String :)
x = "Hello,everyone"
print(x[0:3]) # it will print from index 0 to before 3 ( 3 is not included )

print(x[:2]) # it will only print till 2

print(x[2:]) # it will print everything except anything before index 2

print(x[-5:-2]) # it will print from the -5 char before ending of the string till the -2 char before ending of the string
print("----------------------------------------------------------------------------")
#Modify Strings
text = "Hello ,cats ^^  "
print(text.upper()) # it will change the string to uppercase
print(text.lower()) # it will change the string to lowercase

print(text.strip()) # it will remove the whitespace it will print "Hello cats ^^"
print(text.replace("H","Y")) # replace a char
print(text.split(",")) # Split the string using a subtracter 
print("----------------------------------------------------------------------------")
# Add two strings using "+"
x = "Hello"
y = "Rakan"
print(x+y) # it will connects the two strings without any whitespace
print(x + " " + y) # it will connect them with a whitespace between them
print("----------------------------------------------------------------------------")
# String format :)
age = 22
text = "Hello my name is rakan and my age is {}"
print(text.format(age))
print("------------------------------")
# same but longer format 
TEXT = "Hello my name is {} i am a FCIT student and my GPA is {}. Also, i will work hard to get {} salary :)"
name = "Rakan"
GPA = 4.63
Salary = 70000
print(TEXT.format(name,GPA,Salary))

# We can arrange the attributes in the String inside the {}. 
TEXT = "Hello my name is {2} i am a FCIT student and my GPA is {0}. Also, i will work hard to get {1} salary :)"
print(TEXT.format(name,GPA,Salary)) # name will take {0} and so on..
print("----------------------------------------------------------------------------")
# Things we can type inside a String that will get changed :)
print('It\'s alright.')
print("This will insert one \\ (backslash).")
print("Hello\nWorld!")
print("Hello\rWorld!")
print("Hello\tWorld!")
print("Hello \bWorld!")
print("Hello\fWorld!")

print("\110\145\154\154\156") # it will take each number and make it as a char:)
print("\x48\x65\x6c\x6c\x6f") # it will take each hexa and make it as a string

## There are many other methods that we can get an advantage from it in Strings, you can search in the internet :)
## Example : swapcase() , find() , count() and more.. 