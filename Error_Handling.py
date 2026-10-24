# Error Handling :
#     Error handling allow user to handle error at runtime.
#     When  we have a error at runtime program stop execution so to avoid this type of
#         situation during live project we can use error handling methods.

#     Types of Error handling methods
#         try :
#             Try block is use to write a actual logic of our application.
#             When we have complex mthod or logic implemented then we can use error handling.
#             If code does not have any error then try block execute successfully.

#         except :
#             Except block execute when we have a error in try block.
#             If any run time error occured during code execution then except will handle that
#                 error and continue executing code.
#             We have a diff type of Exception.

#             Syntax :
#                 try:
#                     Logic implementation
#                 except:
#                     error handling

#             Example :
try:
    val1 = 10
    val2 = 0

    val3 = val1/val2
    print(val3)
except:
    print('Divide by zero is not possible')

# Ex : 2
try:
    val1 = 10 # int(input("Enter value 1 : "))
    val2 = 20 # int(input("Enter value 2 : "))

    if val2 == 0:
        print("Value2 can not be zero")
        raise 

    val3 = val1/val2
    print(val3)
except ZeroDivisionError:
    print('Divide by zero is not possible')
except:
    print("Something Wrong")
    
#         else :
            # Else block execute when try block execute successfully otherwise else block
            #     will not execute.

            # Syntax :
                # try:
                #     python logic
                # except:
                #     error handling
                # else:
                #     python logic
            
            # Example :

try:
    value1 = int(input("Enter value 1 : "))
    value2 = int(input("Enter value 2 : "))

    if value2 == 0:
        raise
except:
    print("Something wrong")
else:
    value3 = value1 / value2
    print(value3)

#         finally :
            # Finally block always execute if code has error or not.

            # Syntax :
            #     try:
            #         pythin logic
            #     except:
            #         error handling
            #     finally:
            #         logic

            # Example :
print("Finally block example")
try:
    value1 = 10
    value2 = 10

    value3 = value1 / value2
except:
    print("Error generated")
finally:
    print("Finally block executed")
