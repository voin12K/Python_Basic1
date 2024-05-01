class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        super().move()
        print("attention")

    def load(self):
        import time
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print("max speed is", self.max_speed)

truck1 = Truck("Volvo", 3, "XC90", 5000)
truck2 = Truck("Mercedes", 2, "Actros", 10000, color="white")

car1 = Car("Toyota", 5, "Camry", 180, color="blue", weight=1500)
car2 = Car("BMW", 4, "X5", 220)

print("Truck 1:")
truck1.move()
truck1.load()
print("Truck 2:")
truck2.move()
truck2.load()

print("Car 1:")
car1.move()
print("Car 2:")
car2.move()
