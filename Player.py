class Player:

    def __init__(self, race):
        self.name = race.name
        self.fk = race.fk
        self.rating = self.fk
        self.sc = race.sc
        self.health = race.health
        self.attack = None
