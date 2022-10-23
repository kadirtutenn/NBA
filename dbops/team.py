from .base import Base


class team(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "teams")

    def create(self, team):
        self.cursor.execute(
            "INSERT INTO teams VALUES(NULL, ?, ?)",
            (
                team["name"],
                team["season"],
            ),
        )
        self.conn.commit()

    def update(self, team):
        self.cursor.execute(
            "UPDATE teams SET name=?, season=? WHERE id=?",
            (
                team["name"],
                team["season"],
                team["id"],
            ),
        )
        self.conn.commit()

    def get_by_id(self, id):
        Team = {}
        try:
            row = super().get_by_id(id)
            Team["name"] = row["name"]
            Team["season"] = row["season"]
            Team["id"] = row["id"]
        except:
            Team = None

        return Team

    def get_all(self):
        Teams = []
        try:
            rows = super().get_all()
            for row in rows:
                Team = {}
                Team["name"] = row["name"]
                Team["season"] = row["season"]
                Team["id"] = row["id"]
                Teams.append(Team)
        except:
            Teams = None
        return Teams


Team = team("testing.db")
