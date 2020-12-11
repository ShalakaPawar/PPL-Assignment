from Animal import DomesticAnimal # from the Animal.py file import the DomesticAnimal class

class Dog(DomesticAnimal): # Child class of DomesticAnimal
    def __init__(self, colour = None, age = None):
        super().__init__(12, colour, age)
        return

    def sound(self):
        print("I bark!")
        return

    def info(self):
        super().info()
        print("I was the first species to be domesticated, and have been selectively bred over millennia for various behaviors, sensory capabilities, and physical attributes")
        return

    def ability(self):
        print("I am the only animal capable of intuitively understanding human gestures, such as pointing")
        return

    def interestingFact(self):
        print("I have twice as many ear muscles as humans, and I can hear sounds four times better than you!")
        return

    def eat(self):
        print("I like bones")
        return

class Cat(DomesticAnimal):
    def __init__(self, colour = None, age = None):
        super().__init__(12, colour, age)
        return

    def sound(self):
        print("Meow Meow!")
        return

    def info(self):
        super().info()
        print("I am the only domesticated species in the cat family. There are about 60 different cat breeds")
        return

    def ability(self):
        print("My tail helps me balance myself while climbing on a tree or when making a sharp turn while running")
        return

    def interestingFact(self):
        print("There are cats who have survived falls from over 32 stories (320 meters) onto concrete")
        return

    def eat(self):
        print("I eat mice")
        return

d1 = Dog("Golden Yellow", 8)
d1.sound()
d1.info()
d1.ability()
d1.interestingFact()
d1.place()
d1.eat()
print("Lifespan is", d1.lifeSpan())
print("Colour is", d1.getColour())
print("Age is", d1.getAge())
