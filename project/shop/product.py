import random

class Product:

    def __init__(self, product_id, name, description, barcode, category_id):
        self._id = product_id
        self._description = description
        self._barcode = barcode
        self.name = name
        self.category_id = category_id

    def get_id(self):
        return self._id

    def __str__(self):
        return f'{self._id} - {self.name}'


class ProductItem:
    def __init__(self, product, count, price):
        self._id = random.randint(1, 10000)
        self._product = product
        self._count = count
        self._price = price

    def get_id(self):
        return self._id

    def get_product(self):
        return self._product

    def __str__(self):
        return f'{self._id} - {self._product.name} - {self._price} KZT - {self._count}'

