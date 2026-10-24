#Inheritance Example 2
class class_A():
    def __init__(self,name):
        self.name = name    

    def message(self):
        print("This is class A method " + self.name)

class class_B(class_A):
    def __init__(self, name):
      self.message(name)

    def message(self):
        print("This is class B method")

b = class_B("Test A")
b.message()