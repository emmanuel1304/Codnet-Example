"""The Shelter class. Imports from animals, extras.badges, and the stdlib.

Relative imports (the `from .` lines below) only work when this file is
imported as part of the package, so running it directly fails:

    python petshelter/shelter.py     ImportError: attempted relative import...
    python -m petshelter.shelter     works - dots, and no .py on the end

Trigger that error on purpose once, so you recognise it later.
"""

import json
from pathlib import Path

from .animals import create
from .extras.badges import badge_for

# Keeps the save file next to this module, whatever folder you run from.
DATA_FILE = Path(__file__).with_name("shelter.json")


class Shelter:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def __len__(self):
        return len(self.animals)

    def admit(self, species, name, age):
        # animals.py is the expert on building animals, so we delegate.
        animal = create(species, name, age)
        self.animals.append(animal)
        return animal

    def find(self, name):
        """Return the first animal with this name, or None."""
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                return animal
        return None

    def adopt(self, name):
        """Remove an animal by name and return it, or None if not found."""
        animal = self.find(name)
        if animal is not None:
            self.animals.remove(animal)
        return animal

    def roll_call(self):
        """One line per animal, using all three of our modules."""
        return [
            f"{badge_for(animal.age)} {animal} says {animal.speak()}"
            for animal in self.animals
        ]

    def save(self, path=DATA_FILE):
        """Write the animals to a JSON file."""
        rows = [
            {"species": type(a).__name__.lower(), "name": a.name, "age": a.age}
            for a in self.animals
        ]
        Path(path).write_text(json.dumps(rows, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, name, path=DATA_FILE):
        """Rebuild a shelter from the JSON file, or start empty."""
        shelter = cls(name)
        path = Path(path)
        if path.exists():
            for row in json.loads(path.read_text(encoding="utf-8")):
                shelter.admit(row["species"], row["name"], row["age"])
        return shelter


if __name__ == "__main__":
    demo = Shelter("Test Shelter")
    demo.admit("dog", "Rex", 3)
    demo.admit("cat", "Misty", 10)
    print(f"{demo.name} has {len(demo)} animals:")
    for line in demo.roll_call():
        print(" ", line)
