from random import randint

from rich import print


def monster_room(player):
    options = ["fight", "flee"]
    print()
    print("You stumble into a room full of zombies.")
    print("Do you fight or flee?")
    choice = input(">> ").lower()
    if choice not in options:
        print("You cannot do that.")
        monster_room(player)
    elif choice == "flee":
        player.consume_energy(2)
    elif choice == "fight":
        number = randint(0, 10)
        player.take_damage(5)
        print("You killed all the zombies.")
        if number == 5:
            print("A zombie dropped a sword.")
            player.pick_up_item("sword")
