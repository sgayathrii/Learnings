class Person():
    def walk(self):
        return "walking"

class Staff():
    def work(self):
        return "working"

class Busdriver(Person, Staff):
    def driving(self):
        return "driving the bus"

person = Busdriver()
print(person.walk())
print(person.work())
print(person.driving())

    