from system import System
from users.admin import Admin
from users.user import UserRole


def run():
    super_admin = Admin('admin', 'admin@gmail.com', 'test1234', UserRole.SUPER_ADMIN)
    System.super_admin = super_admin
    system = System()
    system.run()


if __name__ == '__main__':
    run()


