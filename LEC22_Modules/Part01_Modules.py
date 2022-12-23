#Consider a module to be the same as a code library.

#A file containing a set of functions you want to include in your application.
import mymodule
mo.greeting("Jonathan")
# We can rename the module that we called into something else by:
import mymodule as mo

mo.greeting("Jonathan")
#if we want to import a thing instead of everything
# we can do it like this:
from mymodule import person1 # we will only call person1
