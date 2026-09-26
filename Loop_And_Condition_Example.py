# I need to insert,delete,updare data in list.
# We need to give options to use to select and based on user input we will 
#   Insert, update or delete data in list.

list = []

while True:
    print('\n1. Insert\n2. Update\n3. Delete\n4. Print')

    choice = input('Enter Choice : ')
    match int(choice):
        case 1: #Insert
            value = input('Enter Value : ')
            list.append(value)
        case 2: # Update
            index = input('Enter index to update value : ')
            update_value = input('Enter new value : ')
            list[int(index)] = update_value
        case 3: # Delete
            delete_value = input('Enter value to remove : ')
            list.remove(delete_value)
        case 4: # Print
            for item in list:
                print(item)        

