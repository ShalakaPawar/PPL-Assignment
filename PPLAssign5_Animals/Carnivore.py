from Animal import WildAnimal # from Animal.py file import the WildAnimal class

class Carnivore(WildAnimal):
    def __init__(self, lifeSpan, colour, age):
        super().__init__(lifeSpan, colour, age)
        return

    def info(self):
        super().info()
        print("I am a Carnivore")
        return

    def eat(self):
        print("I eat Meat!")
        return

class Tiger(Carnivore):
    def __init__(self, colour = None, age = None):
        super().__init__(25, colour, age) # Lifespan is 25 years
        return

    def sound(self):
        print("I Meow and Grunt!")
        return

    def info(self):
        super().info()
        print("I the largest member of the cat Family")
        return

    def ability(self):
        print("I am strong and have a strong eyesight!")
        return

    def interestingFact(self):
        print("I love to swim and play in water")
        return

    def place(self):
        super().place()
        print("Rain forests, grasslands, savannas and even mangrove swamps")
        return

    def eat(self):
        super().eat()
        print("I love to eat Antelope, Monkeys, Buffalo")
        return

class Wolf(Carnivore):
    def __init__(self, colour = None, age = None):
        super().__init__(8, colour, age)
        return

    def sound(self):
        print("I growl, bark, whine, yip and whimper")
        return

    def info(self):
        super().info()
        print("Wolves are a class of the canine family and are one of the largest in the family")
        return

    def ability(self):
        print("I have a high sense of loyalty and communication")
        return

    def interestingFact(self):
        print("I am intelligent and cunning as well!")
        return

    def place(self):
        super().place()
        print("I live in deserts or forests and even high up in the snowy tundra")
        return

    def eat(self):
        super().eat()
        print("I love to eat deer, elk, seals, bison and oxen")
        return

class Snake(Carnivore):
    def __init__(self, colour = None, age = None):
        super().__init__(6, colour, age)
        return

    def sound(self):
        print("I hiss and rattle")
        return

    def info(self):
        super().info()
        print("I am long limbless reptile")
        return

    def ability(self):
        print("I can swallow prey three times the size of my mouth")
        return

    def interestingFact(self):
        print("I am found on every continent except Antarctica")
        return

    def place(self):
        super().place()
        print("I live both in terrestrial and acquatic environment")
        return

    def eat(self):
        super().eat()
        print("I eat lizards, birds, small mammals, snails")
        return
        
    

t1 = Tiger("golden", 10)
t1.sound()
t1.info()
t1.ability()
t1.interestingFact()
t1.place()
t1.eat()
print("LifeSpan is", t1.lifeSpan())
print("Colour is", t1.getColour())
