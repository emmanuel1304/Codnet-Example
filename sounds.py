"""A module is just a .py file. Import it and use what's inside."""

VOLUME = "LOUD"

_SECRET_RECIPE = "beef"   # leading underscore means "internal", by convention


def bark(times=1):
    """Return a bark, repeated `times` times."""
    return " ".join(["Woof!"] * times)


def meow():
    return "Meow..."


def tweet():
    return "Tweet tweet"


def mystery_noise():
    return f"(sniffs the {_SECRET_RECIPE})"


# Packing list for `from sounds import *`. mystery_noise is left off on purpose.
__all__ = ["VOLUME", "bark", "meow", "tweet"]


if __name__ == "__main__":
    print(bark(3))
    print(meow())
    print(tweet())
