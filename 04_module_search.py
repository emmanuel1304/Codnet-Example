"""Where Python looks for a module, and the two classic import errors.

Search order: your folder, then PYTHONPATH, then the standard library,
then site-packages. First match wins.

Run:  python 04_module_search.py
"""

import sys

print("=== sys.path, in search order ===")
for position, folder in enumerate(sys.path, start=1):
    print(f"  {position}. {folder or '(this folder)'}")

print("\n=== ModuleNotFoundError ===")
try:
    import pet_sauces
except ModuleNotFoundError as oops:
    print(" ", oops)
    print("  Usual causes: a typo, a missing pip install, or wrong folder.")

print("\n=== __pycache__ ===")
import sounds

print("  read from:", sounds.__file__)
print("  cached as:", sounds.__cached__)
print("  Just a speed cache. Safe to delete, never commit it.")

print("\n=== Shadowing trap ===")
print("  Your folder is searched FIRST, so a file named random.py means")
print("  `import random` finds yours and random.randint() disappears.")
print("  Never name a file random.py, math.py, json.py or test.py.")
