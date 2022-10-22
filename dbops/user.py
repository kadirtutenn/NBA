from .base import Base


class user(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "users")

    def create(self, user):
        self.cursor.execute(
            "INSERT INTO users VALUES(NULL, ?, ?)",
            (
                user.email,
                user.password,
            ),
        )
        self.conn.commit()

    def update(self, user):
        self.cursor.execute(
            "UPDATE users SET email=?, password=? WHERE id=?",
            (
                user.email,
                user.password,
                user.id,
            ),
        )
        self.conn.commit()

    def get_by_email(self, email):
        self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE email=?", (email,))
        return self.cursor.fetchone()


User = user(
    "testing.db",
)


# class deneme:
#     def __init__(self, id, email, password):
#         self.id = id
#         self.email = email
#         self.password = password


# x = deneme(1, "apo@test.com", "121599")
# email = "apo@test.com"
# User.create(x)
# y = User.get_by_email(email)
# print(y["password"])
