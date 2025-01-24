#la herencia multiple en Python permite combinar comportamientos de multiples clases en una sola,
#facilitando la creacion de objetos mas complejos y flexibles.

#Ejemplo de herencia multiple
class Animal:
    def make_sound(self):
        pass

class Walkable:
    def walk(self):
        print("Walking")

class Dog(Animal, Walkable):
    def __init__(self):
        print("Dog created")
        
    def speak(self):
        return "Woof"
    
class Cat(Animal, Walkable):
    def __init__(self):
        print("Cat created")

    def speak(self):
        return "Meow"
    
dog = Dog()
dog.walk()
print(dog.speak())
print("")
cat = Cat()
cat.walk()
print(cat.speak())