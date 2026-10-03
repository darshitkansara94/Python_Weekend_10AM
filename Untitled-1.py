# I need to create a list :
#     1. Type of string values
#     2. Number type of list

# I want to enter a data into this two list based on user selection.
#     Option should be :
#         1. String Value
#         2. Number Value
#         3. Exit

# Select options to perform :
#     1. Insert
#     2. UpdateAs
#     3. Delete
#     4. Print

# I need to perform this using a function / method. Function should be common for both 
#     list.    


string_value = []
number_value = []

def input_list(userchoice,userinput):
    if userinput != 4:
        input_value = input("Enter value : ")

    match userinput:
        case 1:
            if userchoice == 1:
                string_value.append(input_value)
            else:
                number_value.append(input_value)
        case 2:
            index = int(input("Enter index number : "))
            if userchoice == 1:
                string_value[index] = input_value
            else:
                number_value[index] = input_value
        case 3:
             if userchoice == 1:
                string_value.remove(input_value)
             else:
                 number_value.remove(input_value)
        case 4:
             if userchoice == 1:
                for item in string_value:
                    print(item)
             else:
                 for numberitem in number_value:
                     print(numberitem)
        case _:
            print("Invalid Choice")

while True:
    print("\n1. String\n2. Number\n3. Exit")
    userchoice = int(input("Enter list type : "))

    if userchoice == 3:
        break

    print("\n1. Insert\n2. Update\n3. Delete\n4. Print")
    userinput = int(input("Enter your choice : "))
    input_list(userchoice,userinput)

