# Requirement :
#   Add value into list through user.
#   if User want to exit then need to give option for that as well.

list = [] # Create empty list

while True:
    list_value = input("Enter value : ")
    list.append(list_value) 

    print("\nList of values")
    for lst in list:
        print(lst)