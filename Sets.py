# Sets :
#     Sets is a collection of immutable and unordered values.
#     Unorder values means when we write some value in sets and at the run time we will
#         get that value in some other order.
#     We can not modify the sets data at runtime.
#     When we have some static data and data that is not going to change at 
#         runtime then we can use this type of collection.
#     Sets declare with the curly brackets('{}')

#     Syntax :
#         varible_name = {expression1,expression2,....,expressionN}

#     Example :

dictionary = {} # Create blank dictionary
print(type(dictionary))

sets = set({}) # Convert dictionary to set
print(type(sets))

sets_fruits = {'Mango','Banana','Apple','Kiwi'}
print(sets_fruits)

fruit_name = {'Dragon Fruit'}

complete_fruit = (sets_fruits | fruit_name)
print(complete_fruit)

# Clear all the value of sets
sets_fruits.clear()
print(sets_fruits)
