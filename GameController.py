import random
from Warrior import Warrior
from Opponent import Opponent
from Race import Race


class GameController:
    races_array = []

    def __init__(self):
        self.generate_races()

    def generate_races(self):
        yoh = Race("Yoh", 800, 0, 120)
        horo = Race("Horo-Horo", 500, 0, 150)
        ren = Race("Ren", 2000, 0, 120)

        self.races_array = [yoh, horo, ren]

    def create_warrior(self):
        while True:
            choice = input('Please select warrior: 1 - Yoh, 2 - Horo-Horo, 3 - Ren')
            if choice == '1' or choice == '2' or choice == '3':
                break
            else:
                print("Choose valid player")

        warrior_choice = int(choice)
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

            if warrior.health <= 0 or warrior.fk <= 0:
                break

            if opponent.health <= 0 or opponent.fk <= 0:
                win = True
                break

        return win

    def print_status(self, warrior, opponent):
        print('\n')
        print('Your player Furioku: ', warrior.fk, 'Your player Spirit Controll: ', warrior.sc, 'Your player HP: ', warrior.health)
        print('Opponent Furioku: ', opponent.fk, 'Opponent Spirit Controll: ', opponent.sc, 'Opponent HP: ', opponent.health, '\n')

    def attack(self, warrior, opponent):
        # oversoul phase
        while True:
            choice = input('Select oversoul type: 1 - weak, 2 - stable, 3 - gigant')
            if choice == '1' or choice == '2' or choice == '3':
                break
            else:
                print("Choose valid oversoul type")

        spirit_control = int(choice)

        self.select_oversoul(spirit_control, warrior)

        spirit_control = random.randint(1, 3)
        self.select_oversoul(spirit_control, opponent)

        self.print_status(warrior, opponent)

        # attack phase
        while True:
            choice = input('Select attack power lower than spirit control.\n'
                           'If your power less than 30% from spirit control - '
                           'you have a 50% chance to avoid enemies attack.\n'
                           'If your power more than 30% from spirit control - '
                           'enemy 100% attacks you')

            if choice.isdigit():
                warrior.attack = int(choice)
            else:
                print('Type valid attack')
                continue

            if warrior.sc < warrior.attack:
                print('You have no enough spirit control')
            else:
                warrior.sc -= warrior.attack
                break

        opponent.attack = random.randint(1, opponent.sc)
        opponent.sc -= opponent.attack

        self.print_status(warrior, opponent)

        # resolve phase
        if opponent.attack < self.percentage(30, (opponent.sc + opponent.attack)):
            warrior_power = random.randint(0, 1)
        else:
            warrior_power = 1

        if warrior.attack < 100:
            opponent_power = random.randint(0, 1)
        else:
            opponent_power = 1

        opponent = self.resolve(warrior, opponent, warrior_power)
        warrior = self.resolve(opponent, warrior, opponent_power)

        self.print_status(warrior, opponent)
        print("NEW ROUND \n")

    def oversoul(self, player, spirit_control):
        if spirit_control > player.fk:
            spirit_control = player.fk
        player.fk += player.sc
        player.sc = spirit_control
        player.fk -= player.sc

    def select_oversoul(self, spirit_control, player):
        if spirit_control == 1:
            self.oversoul(player, self.percentage(10, player.rating))
        if spirit_control == 2:
            self.oversoul(player, self.percentage(30, player.rating))
        if spirit_control == 3:
            self.oversoul(player, self.percentage(50, player.rating))

    def resolve(self, first, second, power):
        second.sc -= first.attack * power
        first.attack = 0

        if second.sc < 0:
            second.health += second.sc
            second.sc = 0

        return second

    def percentage(self, part, whole):
        return whole / 100 * part
