"""Animal classes - inheritance, overriding and super()."""


class Animal:
    legs = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "..."

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


# Maps the name used in the CLI / data file to the class.
SPECIES = {"dog": Dog, "cat": Cat, "bird": Bird}


def create(species, name, age):
    """Build an animal from a species name. Raises ValueError if unknown."""
    try:
        cls = SPECIES[species.lower()]
    except KeyError:
        raise ValueError(f"unknown species: {species}")
    return cls(name, age)
