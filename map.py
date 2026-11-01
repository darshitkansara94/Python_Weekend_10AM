# map :
#     Map function use to iterate a value through function.
#     It is work with the collections.

#     Syntax :
#         map(function,iteration)

#     Example :

lst = [10,20,30,50]

def sqrt(n):
    return n * n

list_sqrt = (map(sqrt,lst))

print(list(list_sqrt))

# empty_lst = []
# def with_function():
#     for i in lst:
#         sqr = i * i
#         empty_lst.append(sqr)

# with_function()
# print(empty_lst)

numbers = ["10","30","50","20"]

converted_list = map(int,numbers)
print(list(converted_list))
print(type(converted_list))