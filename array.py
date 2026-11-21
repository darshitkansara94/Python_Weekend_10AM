# Array :
#     Array is a collection of values where we can store multiple items of same datatype.
#     We need to import libraray with name "array" before used.
#     Index start with the 0.

#     Syntax :
#         import array
#         arr = array.array('i', [1, 2, 3, 4, 5])

#     Example :

import array

arr = array.array('i',[10,30,40,70,20])
print(arr)

print(arr[0])

# Append :
    # Add element at the end of array.

    # Syntax :
    #     arr.append(value)

    # Example :

arr.append(50)
print(arr)

# Give error because array is of type 'i' (integer) and 'Test' is a string.
# arr.append('Test')
# print(arr)

# Insert :
#     Add a value at specific index in the array.

#     Syntax :
#         variable_name.insert(index,value)

#     Example :

arr.insert(3,80)
print(arr)

# Remove :
    # Remove method use to remove value from array by actual value.

    # Syntax :
    #     variable_name.remove(value)

#     Example :

arr.remove(80)
print(arr)

# Throw error if value not found in array.
# arr.remove(2)
# print('Value removed')

# pop :
    # Remove value from array by using the index.

    # Syntax :
    #     variable_name.pop(index)

    # Example :
arr.pop(3)
print(arr)

# Index :
    # Return a value of that element's index in the array.

    # Syntax :
    #     variable_name.index(value)

    # Example :
print(arr.index(30))

# Throw error if value not found in array.
# print(arr.index(80))
    
# Get all the values :
for value in arr:
    print(value)

# Check value is present or not in array before remove :
value = 80

if value in arr:
    arr.remove(value)
    print(arr)
else:
    print('Value not found in array')