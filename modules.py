"""You have been using modules all along: random, math and datetime are modules.

Run:  python 01_modules.py
"""

import math
import random
from datetime import date
import statistics as stats

print("=== Borrowing from the standard library ===")
print("Random dog weight:", random.randint(2, 40), "kg")
print("Square root of 144:", math.sqrt(144))
print("Today:", date.today())
print("Average age:", stats.mean([1, 4, 7, 2]))

print("\n=== A module is an object you can inspect ===")
print("name :", math.__name__)
print("docs :", random.__doc__.strip().splitlines()[0])
print("file :", random.__file__)

# math has no __file__: it was written in C and built into python.exe.
print("math file:", getattr(math, "__file__", "none - built into python.exe"))

print("\n=== What's inside? ===")
tools = [name for name in dir(math) if not name.startswith("_")]
print(f"math offers {len(tools)} tools. First 8:", tools[:8])


def new_func():
    print()