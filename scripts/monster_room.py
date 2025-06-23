def monster_room():
    options = ["fight", "flee"]
    print()
    print("You stumbled into a room full of zombies.")
    print("Do you fight or flee?")
    choice = input(">> ").lower()
    if choice not in options:
        print("You cannot do that.")
        monster_room()
    elif choice == "flee":
        print("You couldn't outrun the monsters. You Died.")
        print("[red]GAME OVER[/red]")
        quit()
    elif choice == "fight":
        print("You killed all the zombies. [green]Good work.[/green]")
