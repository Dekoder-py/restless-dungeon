from random import randint

from rich import print

from scripts.monster_room import monster_room

print("[red]Welcome to the dungeon.[/red]")
print("There are two doors. Do you pick door 1 or 2?")
choice = input(">> ")
try:
    number = int(choice)
except ValueError:
    print("That was not an option.")
monster_num = randint(1, 2)
if number == monster_num:
    monster_room()
else:
    print("That was the way out. You win.")
