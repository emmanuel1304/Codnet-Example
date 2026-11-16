"""Tiny menu-driven front end for the shelter.

Run it with:  python main.py
"""

from shelter import Shelter

MENU = """
--- {name} ({count} animals) ---
1) Admit an animal
2) Roll call
3) Adopt an animal
4) Save and quit
"""


def ask_int(prompt):
    """Keep asking until the user types a whole number."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("  Please type a number.")


def admit(shelter):
    species = input("  Species (dog/cat/bird): ").strip()
    name = input("  Name: ").strip()
    age = ask_int("  Age: ")
    try:
        animal = shelter.admit(species, name, age)
    except ValueError as err:
        print(f"  {err}")
    else:
        print(f"  Welcome, {animal}!")


def roll_call(shelter):
    if not len(shelter):
        print("  The shelter is empty.")
    for line in shelter.roll_call():
        print(f"  {line}")


def adopt(shelter):
    name = input("  Who is going home? ").strip()
    animal = shelter.adopt(name)
    print(f"  {animal} found a family!" if animal else f"  No animal named {name}.")


def main():
    shelter = Shelter.load("Happy Paws")
    actions = {"1": admit, "2": roll_call, "3": adopt}

    while True:
        print(MENU.format(name=shelter.name, count=len(shelter)))
        choice = input("Choose: ").strip()
        if choice == "4":
            shelter.save()
            print("Saved. Bye!")
            return
        action = actions.get(choice)
        if action is None:
            print("  Pick 1-4.")
        else:
            action(shelter)


if __name__ == "__main__":
    main()
