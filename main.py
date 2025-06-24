from random import randint
from time import sleep

from rich import print

from scripts.empty_room import empty_room
from scripts.monster_room import monster_room
from scripts.player import Player
from scripts.rest_room import rest_room


class Game:
    def __init__(self):
        self.player = Player()
        self.last_room = 0
        self.first_room = True

    def enter_room(self):
        rooms = [empty_room, rest_room, monster_room]
        number = randint(0, len(rooms) - 1)
        if number == self.last_room or (self.first_room and number == 1):
            number = randint(0, len(rooms) - 1)
            self.first_room = False
        rooms[number](self.player)
        self.last_room = number
        sleep(2)
        print()
        print()

    def run(self):
        print("[yellow]Welcome to the dungeon.[/yellow]")
        while True:
            self.enter_room()
            print("You continue your journey.")


game = Game()
game.run()
