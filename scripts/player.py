from rich import print


class Player:
    def __init__(self, max_health=80, max_energy=15):
        self.max_health = max_health
        self.max_energy = max_energy
        self.health = self.max_health
        self.energy = self.max_energy
        self.inventory = dict()

    def take_damage(self, damage=5):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print("You ran out of health and died.")
            print("[red]GAME OVER[/red]")
            quit()
        else:
            print(f"You took {damage} damage. Your health is at {self.health}")

    def consume_energy(self, energy_used=5):
        self.energy -= energy_used
        if self.energy <= 0:
            self.energy = 0
            print("You ran out of energy and collapsed.")
            print("[red]GAME OVER[/red]")
            quit()
        else:
            print(f"You consumed {energy_used} energy. Current energy: {self.energy}")

    def pick_up_item(self, item):
        item = item.lower()
        if item not in self.inventory:
            self.inventory[item] = 1
        else:
            self.inventory[item] += 1
        print("New inventory: ")
        for i in self.inventory:
            print(f"{i.title()}: {self.inventory[i]}")

    def rest(self):
        self.health = self.max_health
        self.energy = self.max_energy
        print("You have recovered all your energy and health:")
        print(f"[green]Health: {self.health}[/green]")
        print(f"[green]Energy: {self.energy}[/green]")
