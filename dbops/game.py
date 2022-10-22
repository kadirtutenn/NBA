from base import Base


class Game(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "games")

    def create(self, player):
        pass

    def update(self, player):
        pass
