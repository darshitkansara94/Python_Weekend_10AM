# Inheritance Example
class class_A():
    def message(self):
        print("This is class A")

class class_B(class_A):
    def message_Name(self):
        print("This is class B")

B = class_B() # Object / Instance create for Class B
B.message()
B.message_Name()
