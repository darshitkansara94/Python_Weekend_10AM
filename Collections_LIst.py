# Collections :
#     Collection is a use to store multiple values.

#     Types of collection :
#         List :
            # List can store multiple values with same type of with different type of values.
            # List define with the square brackets.
            # We can add, modify or remove value from the list.
            # In list we can access value through index number.
            # Index always start with the 0.

            # Syntax :
            #     list_name = [expression1,expression2,expression3,...,expressionN]

            # Example :

lst = [] # This is consider as a empty list

fruit_list = ['Mango','Apple','Banana','Kiwi']
print(type(fruit_list))
print(fruit_list)

# Access value from list
print(fruit_list[0])
print(fruit_list[2])

# Add value into existing list
# Insert :
#     Insert method use to insert any value to particular index number.

#     Syntax :
#         insert(index_number,value)

#     Example :

fruit_list.insert(2,'Dragon Fruit')
print(fruit_list)

fruit_list.insert(6,'Watermelon')
print(fruit_list)
print(fruit_list[5])

# print(fruit_list[7]) # This line throw error as index 7 is not present in list.

# Append :
    # Append is also use to insert a value in the list but value always add at the
    #     end of list.

    # Syntax :
    #     append(value)

    # Example :   
fruit_list.append('Pineapple')
print(fruit_list)

# Identify the no of value inside list.
print(len(fruit_list))

# print(dir(fruit_list))

# Copy list
fruit_copy = fruit_list.copy()
print(fruit_copy)

# Remove value from list
# Remove :
#     Remove function use to remove value by using expression.
#     Ex : If i want to remove value 'Mango' by name then i can use remove method.

#     Syntax :
#         remove(expression)

#     Example :

fruit_list.remove('Apple')
print(fruit_list)
    
# pop :
    # Pop method use to remove value through index number.
    # To remove value from list pop is suggested method.

    # Syntax :
    #     pop(index_number)

    # Example :

fruit_list.pop(2)
print(fruit_list)

# Clear method use to remove all value from list
# Clear :
#     Clear function use to remove value from the list.
#     This function only remove the value but the list will be there with the 
#         empty values.

#     Syntax :
#         list_name.clear()

#     Example :

fruit_copy.clear()
print(fruit_copy)

# Revserse :
    # Display list value into reverse order.

    # Example :
fruit_list.reverse()
print(fruit_list)

# Sort :
    # Sort function use to sort a list into ascending or descending order.

    # Syntax :
    #     list_name.sort()

    # Example :
fruit_list.sort() # Print value in  ascending order
print(fruit_list)

fruit_list.sort(reverse=True) # Print value in descending order
print(fruit_list)