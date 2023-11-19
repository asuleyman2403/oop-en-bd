from users.user import User, UserRole


class Admin(User):
    def __init__(self, username, email, password):
        super().__init__(username, email, password, UserRole.SUPER_ADMIN)





