
#Name: Shalaka Pawar
#MIS: 111903095

# Parent class
class Animal(): 
    def __init__(self, lifeSpan = None, colour = None, age = None):
        self._numberOfEyes = 2
        self._numberOfLegs = 4
        self._numberOfEars = 2
        self._lifeSpan = lifeSpan
        self._colour = colour
        self._age = age
        return

    def info(self):
        pass

    def eat(self):
        pass

    def sound(self):
        pass

    def place(self):
        pass

    def ability(self):
        pass

    def interestingFact(self):
        pass

    def getNumberOfEars(self):
        return self._numberOfEars

    def getNumberOfLegs(self):
        return self._numberOfLegs

    def getNumberOfEyes(self):
        return self._numberOfEyes

    def lifeSpan(self):
        return self._lifeSpan

    def getColour(self):
        return self._colour

    def getAge(self):
        return self._age

    def setAge(self, age):
        self._age = age
        return

class WildAnimal(Animal): # Child class of Animal
    def __init__(self, lifeSpan, colour, age):
        super().__init__(lifeSpan, colour, age)
        return

    def info(self):
        print("I am a wild animal")
        return

    def place(self):
        print("I live in the Jungle!")
        return

class DomesticAnimal(Animal): # Child class of Animal
    def __init__(self, lifeSpan, colour, age):
        super().__init__(lifeSpan, colour, age)
        return

    def info(self):
        print("I am a domestic animal")
        return

    def place(self):
        print("I live with humans")
        return
