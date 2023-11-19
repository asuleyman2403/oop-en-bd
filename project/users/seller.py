from users.user import User, UserRole


class Seller(User):
    def __init__(self, username, email, password, product_items):
        super().__init__(username, email, password, UserRole.SELLER)
        self.product_items = product_items

    def add_product_item(self, product_item):
        self.product_items.append(product_item)



