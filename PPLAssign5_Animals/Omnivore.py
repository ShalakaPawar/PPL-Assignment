from Animal import WildAnimal # from Animal.py file import the WildAnimal class

class Omnivore(WildAnimal):
    def __init__(self, lifeSpan, colour, age):
        super().__init__(lifeSpan, colour, age)
        return

    def info(self):
        super().info()
        print("I am an Omnivore")
        return

    def eat(self):
        print("I eat both meat and grass")
        return

class Bear(Omnivore):
    def __init__(self, colour = None, age = None):
        super().__init__(25, colour, age)
        return

    def sound(self):
        print("I huff, whoof, growl!")
        return

    def info(self):
        super().info()
        print("I have a large body with stocky legs, long snouts, small rounded ears, shaggy hair!")
        return

    def ability(self):
        print("I see in color and have sharp vision close-up")
        return

    def interestingFact(self):
        print("A bear fought in the Polish Army in WW2. He carried shells to the frontline and was taught to salute")
        return

    def place(self):
        super().place()
        print("I am found in both open and woody environments")
        return

    def eat(self):
        super().eat()
        print("I eat chickens, fish, seasonal fruits!")
        return

class Gorilla(Omnivore):
    def __init__(self, colour = None, age = None):
        super().__init__(35, colour, age)
        return

    def sound(self):
        print("I belch!")
        return

    def info(self):
        super().info()
        print("Gorillas are large apes that are native to Africa.")
        print("They are typically divided into two groups. Mountain Gorilla and Lowand Gorilla")
        return

    def ability(self):
        print("I have the ability of problem solving")
        return

    def interestingFact(self):
        print("Gorilla shares 90% of its biology with humans")
        return

    def place(self):
        super().place()
        print("I am found in tropical and subtropical forests of sub-Saharan Africa")
        return

    def eat(self):
        super().eat()
        print("I eat seeds, fruits, young branches, insects like termites and ants")
        return

b1 = Bear("Grey", 12)
b1.sound()
b1.info()
b1.ability()
b1.interestingFact()
b1.place()
b1.eat()
print("Lifespan is", b1.lifeSpan())
print("Colour is", b1.getColour())
print("Age is", b1.getAge())
