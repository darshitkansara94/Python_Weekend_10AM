# Dictionary :
#     Dictionary is a collection of values which contains key and value.
#     Every value is associate with some key.
#     We can access value by using the key in dictionary.
#     We can not create a duplicate key in the same ditionary.
#     Dictionary written within curly braackets ({})

#     Syntax :    
#         variable_name = {
#             key : expression1,
#             key : expression2,
#             .
#             .
#             key : expressionN
#         }

#      Example :
# ['Darshit','Kansara',29,'abc@gmail.com','G-411, opp xyz','xyz@gmail.com']

# Firstname = 'Darshit',
# Lastname = 'Kansara',
# Age = 29,
# primaryEmail = 'abc@gmail.com',
# address = 'G-411, opp xyz',
# alternateEmail = 'xyz@gmail.com'

person_info = {
    'firstName' : 'Darshit',
    'lastName' : 'Kansara',
    'age' : 29,
    'primaryEmail' : 'abc@gmail.com',
    'alternameEmail' : 'xyz@gmail.com',
    'address' : 'G-411, opp xyz'
}

print(type(person_info))
print(person_info)

print(person_info['firstName']) # Access value from dictionary using key

# print(dir(person_info))

# Copy :
copy_person_info = person_info.copy()
print(copy_person_info)

# Items :
#    Return all the keys and value from the dictionary.

print(person_info.items())

# Keys :
#    Return all the keys present into the dictionary.

print(person_info.keys())

# Values :
#   Return all the values from the dictionary without key.

print(person_info.values())

# Add value into existing dictionary.
#   We can add any value into the dictionary by using key and value pair.

#   Syntax :
#        dict_Name[key_name] = expression
#   Example :
person_info['mobile_no'] = 8971592749

print(person_info)

# pop :
    # We can remove a value from dictionary by using a  key name.
    # If key is present then it will remove otherwise it will throw error.

    # Syntax :
    #     dict_name.pop(key_name)

    # Example :

person_info.pop('age') # Remove particular key from the dictionary
print(person_info)

person_info.popitem() # Remove last key from the dictionary
print(person_info)

person_info.popitem()
print(person_info)

# Get :
    # We can access value from the dictionary by using key name.
    # If key is not found then it will return none as a O/P.

    # Syntax :
    #     dictionary_name.get('key_name')

    # Example :
print(person_info.get('firstName'))
print(person_info.get('age'))
print(person_info['age'])

# Clear :
    # Clear the values and keys of the dictionary.
    # It will not remove the dictionary but it will remove only values and keys.

    # Example :
# person_info.clear()
# print(person_info)
