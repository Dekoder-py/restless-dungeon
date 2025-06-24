def rest_room(player):
    options = ["yes", "no", "sleep", "leave"]
    print("You entered a peaceful room with a cosy bed.")
    print("It is safe to rest. Do you sleep?")
    choice = input(">> ").lower()
    if choice not in options:
        print("You cannot do that.")
        rest_room(player)
    elif choice == "sleep" or choice == "yes":
        print("You had a wonderful sleep.")
        player.rest()
    else:
        print("You continue your journey.")
