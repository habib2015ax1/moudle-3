class BMW:
    def fuel_type(self): print("Petrol")
    def max_speed(self): print("250 km/h")

class Ferrari:
    def fuel_type(self): print("Petrol")
    def max_speed(self): print("340 km/h")

for car in (BMW(), Ferrari()):
    car.fuel_type()
    car.max_speed()