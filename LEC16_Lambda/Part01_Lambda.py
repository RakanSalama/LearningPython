# We use lambda for anonymous functions for example:
x = lambda a : a + 1
print(x(2))

x = lambda m,n : m * n
print(x(3,2))

x = lambda a,b,c : a + b + c
print(x(1,2,4))

#How we use function with lambda:

def Function(n):
    return lambda m : n + m 

x = Function(2)
print(x(3))
# Another example: 
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))