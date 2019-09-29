import random
from Warrior import Warrior
from Opponent import Opponent
from Race import Race


class GameController:
    races_array = []

    def __init__(self):
        self.generate_races()

    def generate_races(self):
        power_man = Race("Power man", 15, 1.0, 100)
        healthy_man = Race("Healthy man", 10, 1.0, 150)
        skill_man = Race("Skill man", 10, 2.0, 100)

        self.races_array = [power_man, healthy_man, skill_man]

    def create_warrior(self):
        warrior_choice = int(input('Please select warrior: 1 - strong, 2 - healthy, 3 - skill'))
        warrior = Warrior(self.races_array[warrior_choice-1])

        return warrior

    def create_opponent(self):
        opponent_choice = random.randint(0, 2)
        opponent = Opponent(self.races_array[opponent_choice])

        return opponent

    def fight(self, warrior, opponent):
        win = False

        while True:
            self.print_status(warrior, opponent)

            self.attack(warrior, opponent)

            if warrior.health < 0:
                break

            if opponent.health < 0:
                win = True
                break

        return win

    def print_status(self, warrior, opponent):
        print('Your player HP: ', warrior.health)
        print('Opponent    HP: ', opponent.health, '\n')

    def attack(self, warrior, opponent):
        warrior.kick = int(input('Please select kick: 1 - to head, 2 - to body, 3 - to foot = '))
        warrior.block = int(input('Please select block: 1 - to head, 2 - to body, 3 - to foot = '))
        print('\n')
        opponent.kick = random.randint(1, 3)
        opponent.block = random.randint(1, 3)

        if warrior.kick != opponent.block:
            print('You hit an opponent!')
            opponent.health = opponent.health - (warrior.power * warrior.skill)

        if warrior.block != opponent.kick:
            print('Opponent hit you :( ')
            warrior.health = warrior.health - (opponent.power * opponent.skill)

    def resolve(self, warrior, opponent):
        warrior.kick = int(input('Please select kick: 1 - to head, 2 - to body, 3 - to foot = '))
        warrior.block = int(input('Please select block: 1 - to head, 2 - to body, 3 - to foot = '))
        print('\n')
        opponent.kick = random.randint(1, 3)
        opponent.block = random.randint(1, 3)

        if warrior.kick != opponent.block:
            print('You hit an opponent!')
            opponent.health = opponent.health - (warrior.power * warrior.skill)

        if warrior.block != opponent.kick:
            print('Opponent hit you :( ')
            warrior.health = warrior.health - (opponent.power * opponent.skill)
