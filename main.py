class Forest:
    height = 100
    weight = 5
    age = 25
    color_list = 'green'
    breed = "oak"

    def __int__(self):
        print(Forest.height)
        print(Forest.age)
        print(Forest.weight)

tree1 = Forest()
print(tree1)

class Student:
    group = "c2013"

    def __init__(self, age, name=None, height=160):
        print(id(self))
        self.height = height
        self.weight = 60
        self.age = age
        self.name = name

    def printer(self):
        print(self.weight)

    def grow(self, height=10):
        self.height += height

    def __str__(self):
        return (f"I'm student. My name is {self.name} "
                f"and I'm {self.age} years old.")

nick = Student(15, "Nick",200)
kate = Student(16, "Kate", 140)
print(nick)
print(kate)
print(nick.age)
print(kate.age)
print(nick.height)
print(kate.height)
print(nick.group, kate.group)
nick.printer()
kate.grow(25)
print(kate.height)