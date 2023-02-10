class Animals():
    def eat(self):
        return "Eating.. nom... nom.."
        

class Horse(Animals):
    def neigh(self):
        return "neigh!"

class Dog(Animals):
    def bark(self):
        return "voof voof!"


call_animal = Horse()
print(call_animal.eat())
print(call_animal.neigh())
call_animal = Dog()
print(call_animal.bark())