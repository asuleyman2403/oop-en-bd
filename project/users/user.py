
from enum import Enum


class UserRole(Enum):
    SUPER_ADMIN = 'SUPER_ADMIN'
    SELLER = 'SELLER'
    CUSTOMER = 'CUSTOMER'


class User:
    def __init__(self, username, email, password, role):
        self._username = username
        self._email = email
        self._password = password
        self._role = role

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_role(self):
        return self._role
