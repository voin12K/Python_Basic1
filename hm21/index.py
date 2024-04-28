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


car1 = Auto("Toyota", 5, "Camry", color="blue", weight=1500)
car1.move()  # Виводить "move"
print("Car age before birthday:", car1.age)
car1.birthday()
print("Car age after birthday:", car1.age)
