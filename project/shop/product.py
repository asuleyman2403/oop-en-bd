

class Product:

    def __init__(self, product_id, name, description, barcode):
        self._id = product_id
        self._description = description
        self._barcode = barcode
        self.name = name


class ProductItem:
    def __init__(self, product, count, price):
        self._product = product
        self._count = count
        self._price = count


