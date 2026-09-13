# Loop / Iterable Operation :
#     Loop is a iterable operation that execute until the condition gets False.
#     Loop is work with collection and conditions.

#     Types of loops :
#         while :
#             While loop use when we need to execute code based on some condition.
#             Iteration continue until the condition gets false.
#             Once condition is false loop ends and next line of code get execute.
#             After condition in while loop we need to do ':' that indicate the loop condition
#                 ends.
#             In while loop indent is important. 

#             Syntax :
#                 while condition:
#                     python code

#                 print(some_expression)

#             Example :

x = 5
while x <= 10:
    print(x)
    x += 1 # x = x + 1

list = ['Mango','Banana','Kiwi'] # length = 3

i = 1
while i <= len(list): # 0 > 3
    print(list[i - 1])
    i += 1 

i = 0
while i < len(list): # 0 > 3
    print(list[i])
    i += 1 

#        for :
            # For loop allow user to fetch value from collections or fetch every single
            #     char through loop.
            # We don't need to increase number manually like a while loop for loop
            #     will increase that numbers.

            # Syntax :
            #     for variable_name in collection/string:
            #         python code

            # Example :
list1 = [10,7,5,3,90]

print("Execution of For loop")

for i in list1:
    print(i)

for fruit_name in list:
    print(fruit_name)

# fetch value from dictionary
dictionary = {
    'firstName': 'Darshit',
    'lastName':'Kansara',
    'age':29,
    'email':'abc@gmail.com'
}

for keys in dictionary.keys():
    print(keys)

for values in dictionary.values():
    print(values)

print("Print key and value from dictionary \n")

for keys,values in dictionary.items():
    print('key name is ' + keys + ' and value is ' + str(values))