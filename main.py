from random import randint
from time import sleep

from rich import print

from scripts.monster_room import monster_room
from scripts.player import Player
from scripts.rest_room import rest_room


class Game:
    def __init__(self):
        self.player = Player()

    def enter_room(self):
        rooms = [monster_room, rest_room]
        number = randint(0, len(rooms) - 1)
        rooms[number](self.player)
        sleep(2)
        print()
        print()

    def run(self):
        print("[yellow]Welcome to the dungeon.[/yellow]")
        while True:
            self.enter_room()


game = Game()
game.run()
