from system import System
from users.admin import Admin
from users.user import UserRole
from shop.category import Category
from shop.product import Product


def run():
    super_admin = Admin('admin', 'admin@gmail.com', 'test1234')
    System.super_admin = super_admin
    categories = [
        Category(1, 'Laptops'),
        Category(2, 'Phones'),
        Category(3, 'Cosmetics'),
    ]

    products = [
        Product(1, 'Lenovo Yoga', 'Laptop description', '0001', 1),
        Product(4, 'Asus Zenbook', 'Laptop description', '0004', 1),
        Product(2, 'Iphone 15', 'Phones description', '0002', 2),
        Product(3, 'Mask', 'Mask description', '0003', 3)
    ]

    System.products = products
    System.categories = categories
    system = System()
    system.run()


if __name__ == '__main__':
    run()


