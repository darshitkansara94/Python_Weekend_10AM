# Tuple :
#     Tuple is an immutable collection. That mean we can not modify the value after 
#         tuple is created.
#     In term of performance tuple is faster than list.
#     We can write tupple in round brackets.
#     Tuple is a ordered collection.

#     Syntax :
#         variable_name = (expression1,expression2,...,exressionN)

#     Example :

blank_tuple = ()

tuple_singlevalue = (10,)
print(type(tuple_singlevalue))

tuple_string = ('Mango',)
print(type(tuple_string))

tuple_fruit = ('Mango','Apple','Banana')
print(type(tuple_fruit))
print(tuple_fruit)

print(tuple_fruit[0])

print(dir(tuple_fruit))

# tuple_fruit[1] = 'Kiwi' # Throw error because we can not modify tuple once it is created.
# print(tuple_fruit)

# To add a value in tuple we need to use casting
tuple_list = list(tuple_fruit)
print(type(tuple_list))
print(tuple_list)
tuple_list.insert(2,'Kiwi')
list_tuple = tuple(tuple_list)
print(list_tuple)

# To add a value in tuple using + operator
tuple1 = (10,20,30)

tuple2 = (40,50)  + tuple1 

print(tuple2)
