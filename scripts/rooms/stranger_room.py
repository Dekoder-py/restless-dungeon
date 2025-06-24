from math import floor
from random import randint

from rich import print


def stranger_room(player):
    print("[yellow]You enter a dimly lit room. There is a strange man standing in the corner.[/yellow]")
    print("Do you approach the man?")
    choice = input(">> ")
    approaches = ["approach", "talk", "walk up to him", "yes", "y", "yep", "ok", "okay", "sure", "ye", "yeah", "yea",
                  "yah"]
    if choice in approaches:
        if randint(0, 1) == 0:
            print("The strange man turns to you and smiles.")
            print("You feel a warm and calming energy.")
            player.energy = player.max_energy
            print("[green]Your energy is restored.[green]")
            print(f"[green]Energy: {player.energy}[/green]")
        else:
            print("[red]The strange man turns to you and scowls.[/red]")
            print("[red]You feel a sharp pain and a cloud of fog enters your mind.[/red]")
            player.take_damage(floor(player.health / 100 * 20))  # damage 20% of current health (rounded)
            player.consume_energy(floor(player.energy / 100 * 50))  # consume 50% of current energy (rounded)
