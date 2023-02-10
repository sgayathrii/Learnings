import mymodule

mymodule.func_in_mymodule()
#if we try to call the variable

print(s) # It may not work


#another way
import mymodule as m

m.func_in_mymodule()

#one more way
from mymodule import func_in_mymodule

func_in_mymodule()

#we can also do like this
from mymodule import *

func_in_mymodule()
#if we try to call the variable

print(s) # it prints the output..