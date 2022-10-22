from base import Base


class Player(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "players")

    def create(self, player):
        pass

    def update(self, player):
        pass


class deneme:
    def __init__(self, id, fullname, username, age):
        self.id = id
        self.fullname = fullname
        self.username = username
        self.age = age


x = deneme(1, "apo", "simsek", 22)
print(x.__dict__.keys())
