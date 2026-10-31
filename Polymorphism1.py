class Dog():
    def sound(self):
        print("Dog barks")

class Cat():
    def sound(self):
        print("Cat meows")

class tiger():
    def sound(self):
        print("Tiger roars")

def animal_sounds(animal):
    animal.sound()

d = Dog()
c = Cat()
t = tiger()

animal_sounds(d)
animal_sounds(c)
animal_sounds(t)
