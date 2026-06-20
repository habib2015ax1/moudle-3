class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class bus(Vehicle):
    pass

school_bus=bus("school volvo",180,400)
print("vehicle Name:", school_bus.name, "speed:",school_bus.max_speed, "mileage:", school_bus.mileage)