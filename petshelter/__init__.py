"""The petshelter package: a folder of related modules.

    petshelter/
    |-- __init__.py   <- runs once, when the package is first imported
    |-- animals.py
    |-- shelter.py
    `-- extras/       <- a sub-package
        |-- __init__.py
        `-- badges.py
"""

__version__ = "1.0"

# Relative import: the dot means "this package". Re-exporting here lets
# people write `from petshelter import Dog` instead of the long path.
from .animals import Animal, Bird, Cat, Dog, create

# Shelter is left out on purpose so shelter.py can still be run with
# `python -m petshelter.shelter` without being imported twice.

__all__ = ["Animal", "Dog", "Cat", "Bird", "create", "welcome"]


def welcome():
    return f"Welcome to the shelter! (petshelter v{__version__})"
