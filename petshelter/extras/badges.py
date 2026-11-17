"""Age badges. Exists to show that a module three folders deep imports fine."""

import modules

def badge_for(age):
    """Return a badge for an animal of this age."""
    if age < 1:
        return "[BABY]"
    if age < 3:
        return "[YOUNGSTER]"
    if age < 8:
        return "[GOOD CITIZEN]"
    return "[WISE ELDER]"


if __name__ == "__main__":
    for age in (0, 2, 5, 12):
        print(age, "->", badge_for(age))
