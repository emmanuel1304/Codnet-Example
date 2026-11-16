"""The Shelter class - holds animals and saves them to a JSON file."""

import json
from pathlib import Path

from animals import create

DATA_FILE = Path(__file__).with_name("shelter.json")


class Shelter:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def __len__(self):
        return len(self.animals)

    def admit(self, species, name, age):
        animal = create(species, name, age)
        self.animals.append(animal)
        return animal

    def find(self, name):
        """Return the first animal with this name, or None."""
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                return animal
        return None

    

    def roll_call(self):
        return [f"{animal} says {animal.speak()}" for animal in self.animals]

    def save(self, path=DATA_FILE):
        rows = [
            {
                "species": type(a).__name__.lower(),
                "name": a.name,
                "age": a.age,
            }
            for a in self.animals
        ]
        Path(path).write_text(json.dumps(rows, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, name, path=DATA_FILE):
        shelter = cls(name)
        path = Path(path)
        if path.exists():
            for row in json.loads(path.read_text(encoding="utf-8")):
                shelter.admit(row["species"], row["name"], row["age"])
        return shelter
