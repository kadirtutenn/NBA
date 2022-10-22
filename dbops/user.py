from base import Base


class User(Base):
    def create(self, user):
        self.cursor.execute(
            "INSERT INTO users VALUES(NULL, ?, ?, ?, ?, ?, ?)",
            (
                user.fullname,
                user.username,
                user.password,
                user.email,
                user.gender,
                user.birthday,
            ),
        )
        self.conn.commit()

    def update(self, user):
        self.cursor.execute(
            "UPDATE users SET fullname=?, username=?, email=?, birthday=?, password=?, gender=? WHERE id=?",
            (
                user.fullname,
                user.username,
                user.email,
                user.birthday,
                user.password,
                user.gender,
                user.id,
            ),
        )
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM users WHERE id=?", (id,))
        self.conn.commit()

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM users WHERE id=?", (id,))
        return self.cursor.fetchone()
