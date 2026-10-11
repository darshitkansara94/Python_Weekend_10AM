# Operators :
#     Operators are use to perform concatenation, calculation or perform some logic with the 
#         symbol.

#     Types of Operators :
#         Arithmetic Operator :
#             Arithmetic operator are use to perform mathemetical operations.

#             Types of Arithmetic Operator:
#                 Addition (+) :
#                     Addition use to perform addition of two or more than two values.

#                     Example :

print(1 + 1)

#                 Substraction (-) :
#                    Minul value from one to another.
#
#                       Example :
print(10 - 5)

#                 Division (/) :
#                   Divide one value to another.
#
#                   Example :

print(10/2) # 5
# print(10/0) # Throw error 

#                 Multiplication (*) :
#                   Multiply numbers
#
#                   Example :

print(10 * 10)

#                 Modulos (%) :
#                   Modulos is a reminder in division.
#
#                   Example :
print(10 % 2)
print(10 % 3)

#                 Floor Division (//) :
#                   When we divide a value, this operator return floor value.
#
#                   Example :
print(10 // 2)

#                 Exponential (**)
#                   Exponential return square root of the value.
#
#                   Example :
print(10 ** 10) # 10 * 10 * 10 *10 *10*10*10*10*10*10
print(5 ** 2) # 5 * 5

#         Assignment Operator :
#           Assignment operator use to assign a value.

#           Types of Assignment Operator :
#               Equal to (=):
#                   Equal to operator use to assign value to the left side variable.
#                   Syntax :
#                       variable_name = value

#                   Example :

x = 4
print(x)

#               += (Addition Assignment):
#                   Make addition more simpler and shorter.

#                   Syntax :
#                        variable_name += value

#                   Example :

print("This is Addition Assignment")
x += 4 # x = 4 + 4

# x = 4, x = x + 4
print(x)

#               -= (Substraction Assignement):
#                   Shorter way to perform substraction

#                   Syntax :
#                       variable_name -= value

#
#                   Example :
z = 5
z -= 10 # z = 5 - 10
print(z)

#               *= (Multiplication Assignment):
#                   Multiply the same value.
# 
#                   Syntax :
#                       variable_name *= value
# 
#                   Example :

y = 4
y *= 5 # y = 4 * 5
print(y)            

#               /= (Division Assignment):
#               //= (Floor division assignment):
#               **= (Exponential asignment) :

#         Comparision Operator :
#           Compare two values.
#           When we compare values so output is always true or false.
#           
#           Types of comparision operator :
#               Double equal to (==) :
#                   Double equal to make sure left side value is equal to
#                        right side value.
#                   If not then o/p is false else true.

#                   Syntax :
#                       value1 == value2
#                   Example :
print (10 == 10)
print(10 == '10')

#               Not equal to (!=) :
#                   Return opposite value of o/p.
#
#                   Syntax :
#                        value1 != value2
#
#                   Example :
print(10 != 10)

#               Greater than (>) :
#                   If left side value is greater than right side value
#                       o/p will be true else false.

#                   Syntax :
#                       value1 > value2

#                   Example :
print(10 > 12) # False
print(50 > 10) # True

#               Less than (<) :
#                   If left side value is lesser than right side value then
#                       o/p will be true else false.

#                   Syntax :
#                       value1 < value2
# 
#                   Example :
print(10 < 12) # True
print(50 < 15) # False 

#               Greater then or equal to (>=) :
#                   If left side value is greater or equal to the right side
#                       value then o/p will be true else false.
#
#                   Syntax :
#                       value1 >= value2
#
#                   Example :
print(10 >= 10) # 10 > 10 or 10 == 10

#               Less than or equal to (<=) :
#                   If left side value is less than right side value or equal
#                       to then o/p will be true else false.

#                   Syntax :
#                       value1 <= value2

#                   Example :
print(10 <= 12) # 10 < 12 or 10 == 12

#         Logical Operator :
#           Logical operator are use to combine multiple conditions. 
#           And based on that condition we will execute the code.
#           We will get condition result as True or False.
#           
#           Types of logical operator :
#               And (and) :
#                   Return true if all the conditions are true else false.
#                  
#                   Syntax :
#                       condition1 and conditions2 and...conditionN

#                   Example :

print("Logical AND Operator Example:")
if True and True:
    print("This condition retuen as true")
else:
    print("This condition return as false")

x = 19
y = 20

if x > 10 and y > 15:
    print("Both conditions are true")
else:
    print("At least one condition is false")

#               Or (or) :
#                   Or operator return True if atleast one condition is True.
#                   Syntax :
#                       condition1 or condition2 or...conditionN

#                   Example :
x = 19
y = 20
print("Or Operator")
if x > 10 or y < 15:
    print("At least one condition is true")
else:
    print("Both conditions are false")

#               Not (not) :
#                   Not operator reverse a condition's boolean result.
#                   Syntax :
#                       not condition
#                   Example :

x = 9
if not x > 10:
    print("This condition is true")
else:
    print("This condition is false")

mobile_number = "123456789"  # Example mobile number
if not len(mobile_number) == 10:
    print("Invalid mobile number")


#         Membership Operator :
#           Membership operator use to check / validate wheather a value exists or not inside a collection.

#           Types of membership operator :
#               In (in) :
#                   In operator use to validate either value is exists or not in collection.
#                   If value exists then it will return true else false.

#                   Syntax :
#                       value in collection

#                   Example :

fruits = ["Banana","Apple","Kiwi","Mango"]
print("Mango" in fruits)
print("mango".capitalize() in fruits)
#print("mango" in fruits.lower())

#               Not In (not in) :
#                   Not in operator checks wheather a value is absent from collections.
#                   If value is absent then it will return true else false.

#                  Syntax :
#                      value not in collection

#                   Example :
print("Mango" not in fruits)


#         Identity Operator :
#           Identity operator useto check wheather two variables referen to the same object in memory.
#           It is not mandatory that their values are equal.

#           Syntax :
#                       variable1 is variable2
#                       variable1 is not variable2

#           Types of identity operator :
#               Is (is) :
#                   Is operator checks whether two variables refer to the same object in memory.
#                   If refere to the same object in memory, it will return true else false.

#               Is Not (is not) :
#                   Is not operator checks whether two variables do not refer to the same object in memory.
#                   If they do not refer to the same object in memory, it will return true else false.

#                   Example :

a = [1, 2, 3]
b = a

print(a is b)

a = [10,20,30,40]
b = [10,20,30,40]

print(a is b)
print(a is not b)

#         Ternary Operator :
#           A ternary operator is a shorthand way of writing an if-else statement.
#           This statement use when we need to write a single statement based on a condition.

#           Syntax :
#               value_if_true if condition else value_if_false

            # Simple If else condition
            # if condition:
            #     value_if_true
            # else:
            #     value_if_false

#           Example :
age = 20
status = "Adult" if age >= 20 else "Minor"
print(status)

# if age >= 20:
#     print("Adult")
#     print("Adult age is equal or greater than 20")
# else:
#     print("Minor")

# Marks 80 or above -> Grade A
# Marks 60 to 79 -> Grade B
# Marks 40 to 59 -> Grade C
# Marks below 40 -> Grade D

Marks = 75
grade = "Grade A" if Marks >= 80 else "Grade B" if Marks >= 60 and Marks <= 79 else "Grade C" if Marks >= 40 and Marks <= 59 else "Grade D"
print(grade)