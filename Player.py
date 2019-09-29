class Player:

    def __init__(self, race):
        self.name = race.name
        self.power = race.power
        self.skill = race.skill
        self.health = race.health
        self.kick = None
        self.block = None
