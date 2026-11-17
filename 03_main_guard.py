"""Why every program ends with `if __name__ == "__main__":`.

A file run directly gets __name__ == "__main__".
A file that is imported gets __name__ == its own filename.

Run:  python 03_main_guard.py
"""

import subprocess
import sys

import sounds

# sounds.py prints inside its own __main__ block, but nothing appeared
# above: it was imported, not run, so that block was skipped.
print("my __name__    :", __name__)
print("sounds.__name__:", sounds.__name__)

print("\n=== Same file, run directly instead of imported ===")
result = subprocess.run([sys.executable, "sounds.py"], capture_output=True, text=True)
print(result.stdout.strip())
print("Now its __main__ block ran. The guard is how one file can be both")
print("a runnable program and a quiet module.")
