# Module :
#     Module is a tool which use to reuse the same code in multiple python files.
#     By using keyword 'import' we can use the code of the python file.

#     Syntax :
#         import python_file_name

#     Example :

import Class_Example1

calc = Class_Example1.calculator()

add_mod = calc.addition()
print(add_mod)

# Inbuilt modules.
# Datetime :
    # Datetime module use to get current date and time and with that i can extract value 
    #     from date.
    # To use this we need to import module datetime.

import datetime

current_time = datetime.datetime.now()
print(current_time)

