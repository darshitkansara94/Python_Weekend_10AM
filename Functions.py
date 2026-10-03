# Function :
#     Function is a block of reusable code.
#     We can use function to avoid code dulicacy and and resuse same code multiple times.
#     When code is not duplicate we can make application more redable and lightweight.
#     We can use the same function in the same file or in multiple pyton files by
#         import that module.
#     We need to access the code of function by using the function name.
#     In python function define with the keyword 'def'.

#     Syntax :
#         Default function
#             def function_name():
#                 python code

#         Parameterized function 
#             def function_name(param1,param2,...,paramN):
#                 python code

#   Example :

def printMessage(): # Function create
    print("Good morning")

printMessage() # Calling my function

# Paramerized function
def printMessage_Param(message):
    print(message)

printMessage_Param('Good morning')
printMessage_Param('Good evening')
printMessage_Param('Good Afternoon')
printMessage_Param(10)

# Error Statement :
# No of param and No of argument should be equal.
# def printMessage_Param_Error(message,number):
#     print(message + number)

# printMessage_Param_Error('Good Morning')

# Return Statement :
    # Return statement use to return some value from the function.
    # We can store that value in some variable and consume for next line of codes.

    # Syntax :
    #     def function_name(param1,param2,..,paramN):
    #         python_code
    #         retrun statement

    # Example :

def calculate(val1,val2):
    c = val1 + val2 # c = 10 + 20 = 30, C = 30
    return c #30

calc = calculate(10,20)
print(calc)

# With nullable parameter
# All the params are by default required param. We can make it optional.

def addition(val1,val2,val3 = 0):
    return val1 + val2 + val3

add = addition(10,20)
print(add)

add1 = addition(10,20,20)
print(add1)

# With string value
def print_Name(firstName,middleName = '',lastName = ''):
    return firstName + middleName + lastName

name = print_Name(firstName='Darshit',lastName='Kansara')
print(name)