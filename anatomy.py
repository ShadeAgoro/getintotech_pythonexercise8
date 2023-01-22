# Example Python script

#import is a python module that can show file path
import sys
#argument_count is our variable
#lens is a built-in function that checks the length
#agrv is a vector - list of arguments/perimeters/ inputs
argc = len(sys.argv)
# this is a conditional statement, testing what is in our argument count
# if argument_count is more than 1
# print = then there is too many arguments
# if there is less than one argument, create a variable called where and assign it the value "World" goodbye from number of command line arguments
#comma between hello and where separates two arguments
# Goodbye line is not a part of the conditional
# [] = square brackets for lists
if argc > 1:
    print ('Too many args')
else:
    where = 'World'
    print("Hello", where)
print ('Goodbye from ' + sys.argv[0])
