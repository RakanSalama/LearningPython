# Int 
x = 5
print(type(x))
# String 
x = "Hello"
print(type(x))
# Float 
x = 20.5
print(type(x))
# Complex
x = 1j
print(type(x))

# list 
x = ["apple", "bannana", "cherry"] 
print(type(x))
# Tuple 
x = ("apple", "bannana", "cherry")         # You can change list values 
print(type(x))                             # You can't change tuple values

# Range
x = range(6)
print(type(x))
# Dict
x = {"name" : "John", "age" : 36}
print(type(x))
# Set
x = {"apple", "bannana", "cherry"}
print(type(x))
# frozenSet
x = frozenset({"apple", "bannana", "cherry"})
print(type(x))
# Boolean
x = True
print(type(x))
# Byte
x = b"Hello"
print(type(x))
# Byte Array
x = bytearray(5)
print(type(x))
# MemoryView
x = memoryview(bytes(5))
print(type(x))
# NoneType
x = None 
print(type(x))