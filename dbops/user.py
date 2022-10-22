from base import Base


class User(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "users")

    # def create(self, user):
    #     self.cursor.execute(
    #         "INSERT INTO users VALUES(NULL, ?, ?, ?, ?, ?, ?)",
    #         (
    #             user.fullname,
    #             user.username,
    #             user.password,
    #             user.email,
    #             user.gender,
    #             user.birthday,
    #         ),
    #     )
    #     self.conn.commit()

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


user = User(
    "dasds",
)


class deneme:
    def __init__(self, id, fullname, username, age):
        self.id = id
        self.fullname = fullname
        self.username = username
        self.age = age


x = deneme(1, "apo", "simsek", 22)

user.delete(1)
user.get_by_id(2)
user.create(x)
