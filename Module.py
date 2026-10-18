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

# Get time
time = datetime.datetime.now().time()
print(time)

# Get date
dt = datetime.datetime.now().date()
print(dt)

# Date format
current_date = datetime.datetime.now().date()
custom_format = current_date.strftime('%d-%m-%Y')
print(custom_format)

date_format = current_date.strftime('%d-%B-%Y')
print(date_format)

# Print current day
current_day = datetime.datetime.now().strftime('%A')
print(current_day)

month = current_date.month
print(month)
day = current_date.day
print(day)
year = current_date.year
print(year)

print_year = datetime.datetime.now().strftime('%y')
print(print_year)
print_year1 = datetime.datetime.now().strftime('%Y')
print(print_year1)


print_month = datetime.datetime.now().strftime('%m')
print(print_month)
print_month1 = datetime.datetime.now().strftime('%b')
print(print_month1)
print_month2 = datetime.datetime.now().strftime('%B')
print(print_month2)

# Difference between days using date
date1 = datetime.datetime(2026,10,18)
date2 = datetime.datetime(2026,10,28)

print(date1)
print(date2)

diff = date1 - date2
print(diff.days)