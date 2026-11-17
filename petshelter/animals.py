"""The animal classes.

This module imports nothing: it is the bottom of the pile. Everything
depends on it, it depends on nothing.
"""


class Animal:
    legs = 4                      # class attribute: shared by every Animal

    def __init__(self, name, age):
        self.name = name          # instance attributes: unique to each animal
        self.age = age

    def speak(self):
        return "..."              # subclasses override this

    def play(self):
        return f"{self.name} is playing"

    def __str__(self):
        return f"{self.name} the {type(self).__name__}, age {self.age}"


class Dog(Animal):
    def __init__(self, name, age, breed="mixed"):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return "Woof woof!!"

    def fetch(self):
        return f"{self.name} brings the ball back"


class Cat(Animal):
    def speak(self):
        return "Meow"

    def play(self):
        return f"{self.name} ignores you"


class Bird(Animal):
    legs = 2

    def speak(self):
        return "Tweet"


SPECIES = {"dog": Dog, "cat": Cat, "bird": Bird}


def create(species, name, age):
    """Build an animal from a species name. Raises ValueError if unknown."""
    try:
        cls = SPECIES[species.lower()]
    except KeyError:
        raise ValueError(f"unknown species: {species}")
    return cls(name, age)


if __name__ == "__main__":
    for species in SPECIES:
        animal = create(species, "Test", 4)
        print(animal, "->", animal.speak(), f"({animal.legs} legs)")
