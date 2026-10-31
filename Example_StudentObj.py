# Multiple Students: 
# Create two student objects with different names and marks. Display their details using the same method.

class student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = student("Alice", 85)
s2 = student("Bob", 90)

s1.display_details()
s2.display_details()