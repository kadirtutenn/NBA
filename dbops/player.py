from .base import Base


class player(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "players")

    def create(self, player):
        self.cursor.execute(
            "INSERT INTO players VALUES(NULL, ?, ?)",
            (
                player["name"],
                player["surname"],
            ),
        )
        self.conn.commit()

    def update(self, player):
        self.cursor.execute(
            "UPDATE players SET name=?, surname=? WHERE id=?",
            (
                player["name"],
                player["surname"],
                player["id"],
            ),
        )
        self.conn.commit()

    def get_by_id(self, id):

        Player = {}
        try:
            row = super().get_by_id(id)
            Player["name"] = row["name"]
            Player["surname"] = row["surname"]
            Player["id"] = row["id"]
        except:
            Player = None

        return Player

    def get_all(self):
        Players = []
        try:
            rows = super().get_all()
            print(rows)
            for row in rows:
                Player = {}
                Player["name"] = row["name"]
                Player["surname"] = row["surname"]
                Player["id"] = row["id"]
                Players.append(Player)
        except:
            Players = None
        return Players


Player = player("testing.db")
