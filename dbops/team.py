from base import Base


class Team(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "users")

    def create(self, team):
        pass

    def update(self, team):
        pass
