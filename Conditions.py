# Conditions :
#     Condition is operation where based on output our code get execute.
#     Output of the condition is always true or false.
#     In condition we have a multiple or single block of code which execute based on
#         output of condition.

#     Types of condition :
#         if else :
#             In If else block we have only two block of codes.
#             Based on output either if or else block got execute.
#             At a time only one block of code get executed.

#             Syntax :
#                 if condition:
#                     code
#                 else:
#                     code
#             Example  :

x = 10
y = 20

if x > y: # 10 > 20 = false
    print('X is greater than y')
else:
    print('X is less than y')


string = 'Hello world'

if type(string) == str:
    print('Yes this is type of string')
else:
    print('This is not type of string')

if  string.lower() == 'hello world':
    print('if executed')
else:
    print('else executed')

#        if elif else :
            # If elif else is extended version of if else.
            # We can verify multiple conditions.

            # Syntax :
            #     if condition:
            #         code
            #     elif condition:
            #         code
            #     elif condition:
            #         code
            #     .
            #     .
            #     .
            #     else:
            #         code

            # Example :

x = 10
y = 30

if x > y:
    print('x is greater than y')
elif x < y:
    print('x is less than y')
elif x == y:
    print('x is equal to y')

#        match expression :
            # match expression is simple to execute and we have a different cases to execute.
            # Working scenerio is similar to the if else and if elif else.

            # Syntax :
            #     match expression:
            #         case condition:
            #             code
            #         case condition:
            #             code
            #         .
            #         .
            #         case _:
            #             default condition
            #   Example :

x = 20
match x: #x = 10
    case 5: # x == 5
        print('value of x is 5')
    case 8: # x == 8
        print('value of x is 8')
    case 10: # x == 10
        print('value of x is 10')
    case _:
        print('value is not matched')

y = 5

match y:
    case '1':
        print('case 1')
    case '2':
        print('case 2')
    case '3':
        print('case 3')
    case '4':
        print('case 4')
    case '5':
        print('case 5')
    case _:
        print('Default')

# z = 10

# match type(z):
#     case str:
#         print('value is in string type')
#     case int:
#         print('value is in integer')
#     case _:
#         print('Undefined Type')
