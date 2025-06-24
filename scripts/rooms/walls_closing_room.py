from rich import print


def walls_closing_room(player):
    print("You walk into a narrow hallway and hear a click.")
    print("[red]The walls creak and start moving towards you.[/red]")
    print("You sprint to the other side, escaping with minor scratches.")
    player.take_damage(3)
    player.consume_energy(5)
