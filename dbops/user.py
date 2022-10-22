from tkinter.messagebox import NO
from .base import Base


class user(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "users")

    def create(self, user):
        self.cursor.execute(
            "INSERT INTO users VALUES(NULL, ?, ?)",
            (
                user["email"],
                user["password"],
            ),
        )
        self.conn.commit()

    def update(self, user):
        self.cursor.execute(
            "UPDATE users SET email=?, password=? WHERE id=?",
            (
                user["email"],
                user["password"],
                user["id"],
            ),
        )
        self.conn.commit()

    def get_by_email(self, email):
        User = {}
        try:
            self.cursor.execute(
                f"SELECT * FROM {self.table_name} WHERE email=?", (email,)
            )
            row = self.cursor.fetchone()
            User["email"] = row["email"]
            User["password"] = row["password"]
            User["id"] = row["id"]
        except:
            User = None
        return User

    def get_by_id(self, id):
        User = {}
        try:
            self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE id=?", (id,))
            row = self.cursor.fetchone()
            User["email"] = row["email"]
            User["password"] = row["password"]
            User["id"] = row["id"]
        except:
            User = None

        return User

    def get_all(self):
        Users = []
        try:
            self.cursor.execute(f"SELECT * FROM {self.table_name}")
            rows = self.cursor.fetchall()
            print(rows)
            for row in rows:
                User = {}
                User["email"] = row["email"]
                User["password"] = row["password"]
                User["id"] = row["id"]
                Users.append(User)
        except:
            Users = None
        return Users


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
