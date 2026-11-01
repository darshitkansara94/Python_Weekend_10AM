# Lambda :
#     Lambda is a shorter version of function define.
#     It can exeute single statement . But if we want to execute multiple line of code / 
#         statement then we need to create function.
#     We can integrate lambda with map function.

#     Syntax :
#         lambda var_name: statement

#     Example :

lst = [10,20,50,40] 

lst_sqr = map(lambda x: x * x,lst)
print(list(lst_sqr))