def rest_room(player):
    print("You enter a peaceful room with a cosy bed.")
    print("It is safe to rest. Do you sleep?")
    choice = input(">> ").lower()
    continues = ["y", "ye", "ya", "yah", "yes", "yeah", "okay", "ok", "sure", "i guess", "yea"]
    nos = ["n", "na", "no", "nah", "nope", "no way", "no thanks"]
    if choice in continues:
        print("You had a wonderful sleep.")
        player.rest()
    elif choice in nos:
        pass
    else:
        print("You cannot do that.")
        rest_room(player)
