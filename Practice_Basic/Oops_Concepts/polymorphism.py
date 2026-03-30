# 👉 Concept
# Same method, different behavior

class Car:
    def __init__(self, *args):
        # print(args)
        self.brand = args[0]
        self.model = args[1]

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()


# #############################################################################
# #############################################################################


class Bird:
    def sound(self):
        print("Some sound")


class Sparrow(Bird):
    def sound(self):
        print("Chirp Chirp")


class Crow(Bird):
    def sound(self):
        print("Caw Caw")


birds = [Sparrow(), Crow()]

for b in birds:
    b.sound()
