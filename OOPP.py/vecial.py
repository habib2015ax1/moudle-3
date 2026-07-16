class Vehicle:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def show(self):
        print("Car:", self.name)

c = Car("BMW")
c.show()
print(issubclass(Car, Vehicle))