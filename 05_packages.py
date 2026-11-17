"""A package is a folder of modules. The dots are folder slashes.

petshelter.extras.badges  ==  petshelter/extras/badges.py

Run:  python 05_packages.py
"""

import sys

import petshelter 
from petshelter.shelter import Shelter              # a module inside the package
from petshelter.extras.badges import badge_for      # inside the sub-package
from petshelter.extras import badge_for as quick    # short path, via __init__.py

print("=== import petshelter ===")
print(petshelter.welcome())
print("version:", petshelter.__version__)
print("Dog, re-exported by __init__.py:", petshelter.Dog)

print("\n=== from petshelter.shelter import Shelter ===")
home = Shelter("Happy Paws")
home.admit("dog", "Rex", 3)
home.admit("cat", "Misty", 1)
home.admit("bird", "Kiwi", 9)
for line in home.roll_call():
    print(" ", line)

print("\n=== the sub-package ===")
print("puppy badge:", badge_for(0), "| old cat badge:", badge_for(14))
print("same function by the short path?", quick is badge_for)

print("\n=== a package is a folder, a module is a file ===")
print("__file__:", petshelter.__file__, "<- a package's __file__ is its __init__.py")
print("__path__:", list(petshelter.__path__), "<- only packages have this")

print("\n=== ours, now loaded ===")
for name in sorted(n for n in sys.modules if n.startswith("petshelter")):
    print(" ", name)
