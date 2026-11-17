# Modules & Packages

A **module** is a `.py` file you can import. A **package** is a folder of
modules. Every file here is runnable, and the lesson files print their own
explanations as they go.

## Run order

| File | Topic |
|---|---|
| `01_modules.py` | `random`, `math`, `datetime` were modules all along. `__name__`, `__file__`, `__doc__`, `dir()` |
| `02_imports.py` | The four import styles, why `import *` is a trap, and the `sys.modules` cache |
| `03_main_guard.py` | `if __name__ == "__main__":` — run directly vs. imported |
| `04_module_search.py` | `sys.path` order, `ModuleNotFoundError`, `__pycache__`, name shadowing |
| `05_packages.py` | Folders as packages, `__init__.py`, sub-packages, dotted paths |
| `main.py` | The finished app — a 50-line entry point |

`sounds.py` is the hand-made module used by lessons 2–4.
`petshelter/` is the package used by lesson 5 and `main.py`.

```
Python Lessons/
├── sounds.py          ← a module on its own
├── 01_modules.py … 05_packages.py
├── main.py            ← entry point
└── petshelter/        ← a package
    ├── __init__.py
    ├── animals.py
    ├── shelter.py
    └── extras/        ← a sub-package
        ├── __init__.py
        └── badges.py
```

## Cheat sheet

```python
import math                  # whole module; math.sqrt()
from math import sqrt        # one name; sqrt()
import statistics as stats   # nickname; stats.mean()
from math import *           # everything, no surnames — don't

import petshelter                                  # a package
from petshelter.shelter import Shelter             # a module inside it
from petshelter.extras.badges import badge_for     # inside a sub-package
from .animals import create    # relative: "this package" (only works inside one)
```

`petshelter.extras.badges` is the path `petshelter/extras/badges.py` with
the slashes swapped for dots.

## Errors worth triggering on purpose

1. **Relative import**
   ```
   python petshelter/shelter.py    # ImportError: attempted relative import...
   python -m petshelter.shelter    # works
   ```
2. **Shadowing.** Create `random.py` containing `print("gotcha")`, run
   lesson 1, watch `random.randint` disappear. Delete it afterwards.
3. **`ModuleNotFoundError`.** Typo an import name and read the message.

## Teaching notes

- **`__init__.py`** runs once when the package is first imported. Its job
  is putting the useful names on the front counter, so students can write
  `from petshelter import Dog`. Python 3.3+ can import a folder without
  one (namespace packages) — mention it, then write one anyway.
- **Why split files?** Point at `main.py` and ask where you'd go to change
  the badge rules. Everyone answers correctly in seconds without having
  read `badges.py`. That's the whole argument for modules.
- **Dependencies point one way.** `animals.py` imports nothing,
  `shelter.py` imports animals + badges + stdlib, `main.py` sits on top.
  Two modules importing each other is a circular import — another day.
- **`__pycache__`** is a bytecode cache, nothing more. It's gitignored.

## Homework

Add a `Rabbit` class and a `petshelter/extras/food.py` module saying what
each species eats. Rules: `main.py` grows by at most two lines, and
`animals.py` must still import nothing.
