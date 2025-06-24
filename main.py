from random import randint
from time import sleep

from rich import print

from scripts.empty_room import empty_room
from scripts.player import Player
from scripts.rest_room import rest_room
from scripts.walls_closing_room import walls_closing_room
from scripts.zombie_room import zombie_room


class Game:
    def __init__(self):
        self.player = Player(self)
        self.last_room = 0
        self.first_room = True
        self.level_count = 0

    @staticmethod
    def over(death_type):
        print(f"You ran out of {death_type} and died.")
        print("[red]GAME OVER[/red]")
        quit()

    def enter_room(self):
        rooms = [empty_room, rest_room, zombie_room, walls_closing_room]
        if self.first_room:
            number = randint(2, len(rooms) - 1)
            self.first_room = False
        else:
            number = randint(0, len(rooms) - 1)
            if number == self.last_room:
                number = randint(0, len(rooms) - 1)
        rooms[number](self.player)
        self.last_room = number
        sleep(2)
        print()
        print()

    def run(self):
        print("[yellow]Welcome to the dungeon.[/yellow]")
        sleep(1)
        print()
        while self.level_count < 10:
            self.enter_room()
            while True:
                print("Are you ready to continue your journey?")
                choice = input(">> ").lower()
                continues = ["y", "ye", "ya", "yah", "yes", "yeah", "okay", "ok", "sure", "i guess", "yea",
                             "not really but okay"]
                if choice in continues:
                    print("You continue onwards.")
                    print()
                    break
                else:
                    print("[red]In the dungeon, there is no escape.[/red]")
                    self.player.take_damage(2)
                    print()
                sleep(1.5)
            self.level_count += 1
        print("[green]Congratulations! You reached the end of the dungeon and escaped.[/green]")
        print("[bold]You Win.[bold]")


game = Game()
game.run()
