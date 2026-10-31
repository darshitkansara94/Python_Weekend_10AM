class Animal():
    def sound(self):
        print("Animal makes a sound")

class dog(Animal):
    def sound(self):
        print("Dog barks")

class cat(Animal):
    def sound(self):
        print("Cat meows")

d = dog()
c = cat()

d.sound()
c.sound()
