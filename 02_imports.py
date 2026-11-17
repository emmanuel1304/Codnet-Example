"""The four import styles, using our own sounds.py module.

Run:  python 02_imports.py
"""
import modules
import sounds                              # whole module, keeps its surname
from sounds import meow, tweet             # just these two names
import sounds as snd                        # nickname
from sounds import *                        # everything, no surname - avoid

print("1. import sounds          ->", sounds.bark(2), "| volume:", sounds.VOLUME)
print("2. from sounds import ... ->", meow(), tweet())
print("3. import sounds as snd   ->", snd.bark())
print("4. from sounds import *   ->", bark(), "(where did bark come from?)")

# __all__ in sounds.py left mystery_noise off the list, so * skipped it.
print("   did * bring mystery_noise?", "mystery_noise" in dir())
print("   still reachable properly :", sounds.mystery_noise())

print("\n=== A module is loaded once, then cached ===")
import sys

print("in sys.modules?", "sounds" in sys.modules)
print("snd is sounds? ", snd is sounds)

sounds.VOLUME = "quiet"
print("changed via sounds, read via snd:", snd.VOLUME)

# Styles 2 and 4 copied the name into this file, so our VOLUME is stale.
print("but our `import *` copy is stale:", VOLUME)
