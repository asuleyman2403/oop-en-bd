from users.user import User


class Admin(User):
    def __init__(self, username, email, password, role):
        super().__init__(username, email, password, role)





