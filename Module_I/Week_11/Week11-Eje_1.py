class Circle:
    radius = 0

    def get_area(self):
        pi = 3.14
        circle_area= (pi*(self.radius**2))
        print(f"El area del circulo es {circle_area}")

circulo1 = Circle()
circulo1.radius = 5
circulo1.get_area()