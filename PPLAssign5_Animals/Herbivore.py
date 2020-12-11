from Animal import WildAnimal # from Animal.py import WIldAnimal Class

class Herbivore(WildAnimal):
    def __init__(self, lifeSpan, colour, age):
        super().__init__(lifeSpan, colour, age)
        return

    def info(self):
        super().info()
        print("I am a Herbivore")
        return

    def eat(self):
        print("I eat grasses, herbs, vegetables!")
        return

class Deer(Herbivore):
    def __init__(self, colour = None, age = None):
        super().__init__(12, colour, age)
        return

    def sound(self):
        print("I grown or bawl")
        return

    def info(self):
        super().info()
        print("I am a hoofed grazing or browsing animal, with branched bony antlers that are shed annually and typically borne only by the male")
        return

    def ability(self):
        print("I have a great sense of hearing")
        return

    def interestingFact(self):
        print("Each year my antlers fall off and regrow!")
        return

    def place(self):
        super().place()
        print("I live in a variety of biomes, ranging from tundra to the tropical rainforest")
        return

    def eat(self):
        super().eat()
        print("I eat young leaves, tender shoots and twigs, plants and vines")
        return

class Elephant(Herbivore):
    def __init__(self, colour = None, age = None):
        super().__init__(60, colour, age)
        return

    def sound(self):
        print("I trumpet, rumble and roar!")
        return

    def info(self):
        super().info()
        print("An elephant is the largest land mammal")
        print("They are extremely intelligent and wise creatures and are known to have really good memories")
        return

    def ability(self):
        print("I have significant cognitive abilities, emotional intelligence and very good memory!")
        return

    def interestingFact(self):
        print("My huge ears are used to radiate excess heat away from the body")
        return

    def place(self):
        super().place()
        print("I am found in different habitats, including savannahs, forests, deserts, and marshes")
        return

    def eat(self):
        super().eat()
        print("I eat grass and woody plants")
        return

class Giraffe(Herbivore):
    def __init__(self, colour = None, age = None):
        super().__init__(26, colour, age)
        return

    def sound(self):
        print("I humm!")
        return

    def info(self):
        super().info()
        print("I am the tallset living terrestrial animal and the largest ruminant")
        return

    def ability(self):
        print("I have excellent eye sight")
        return

    def interestingFact(self):
        print("I can live with only 2-3 minutes of sleep every day. I also sleep standing up!")
        return

    def place(self):
        super().place()
        print("I live in Savanna Eco-System")
        return

    def eat(self):
        super().eat()
        print("I like to eat leaves, twigs and fruits")
        return

g1 = Giraffe("Golden Yellow", 12)
g1.sound()
g1.info()
g1.ability()
g1.interestingFact()
g1.place()
g1.eat()
print("Lifespan is", g1.lifeSpan())
print("Colour is", g1.getColour())
print("Age is", g1.getAge())
