class Person:
    def __init__(self, name) -> None:
        self.name = name
        print(f"Se ha creado un objeto de tipo persona y se llama: {self.name}")


class Bus:
    max_passengers = 5
    passengers = 0

    def __init__(self) -> None:
        self.passengers_on = []

    def add_passenger(self, person):
        if self.passengers == self.max_passengers:
            print("Lo sentimos, el Bus esta lleno y debe tomar el proximo.")
        else:
            self.passengers += 1
            print("Pase adelante")
            self.passengers_on.append(person.name)
            print(f"Estos son los pasajeros abordo del autobus en este momento: {self.passengers_on}")

    def remove_passenger(self, person):
        if person.name in self.passengers_on:
            self.passengers_on.remove(person.name)
            self.passengers -= 1
            print(f"{person.name}, se ha bajado del autobus.")
        else:
            print(f"{person.name} no esta en el autobus.")


person_1 = Person("Juan")
person_2 = Person("Ana")
person_3 = Person("Daniela")
person_4 = Person("Andrea")
person_5 = Person("Lucia")
person_6 = Person("Vanessa")
yellow_bus = Bus()
yellow_bus.add_passenger(person_1)
yellow_bus.add_passenger(person_2)
yellow_bus.add_passenger(person_3)
yellow_bus.add_passenger(person_4)
yellow_bus.add_passenger(person_5)
yellow_bus.add_passenger(person_6)
yellow_bus.remove_passenger(person_2)
yellow_bus.add_passenger(person_6)
