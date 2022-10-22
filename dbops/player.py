from base import Base


class Player(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "players")

    def create(self, player):
        pass

    def update(self, player):
        pass
