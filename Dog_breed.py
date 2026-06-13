class Dog:
    animal = "Dog"

    def __init__(self, breed):
        self.breed = breed

dog1 = Dog("Pug")
dog2 = Dog("Beagle")

print(dog1.animal, dog1.breed)
print(dog2.animal, dog2.breed)