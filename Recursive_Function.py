# Recursive Function :
#     Recursive function call itself until the condition gets fail.

#     Syntax :
#         def func_name():
#             property

#             func_name()

#     Example :

def print_numer(n):
    i = 0

    while n > i:
        print(i)
        i = i + 1 

print_numer(5)

# With recursive function
print("With Recursive function")
def rec_Printnumber(n):
    if n == 0:
        return
    else:
        print(n)
        rec_Printnumber(n - 1)

rec_Printnumber(5)

# factorial
# !5 = 1 x 2 x 3 x 4 x 5 = 120 

print("Calculate factorial")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
        
print(factorial(1))
    