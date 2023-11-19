from users.user import User, UserRole


class Customer(User):
    def __init__(self, username, email, password, basket):
        super().__init__(username, email, password, UserRole.CUSTOMER)
        self.basket = basket

    def add_product_to_basket(self, product_item):
        self.basket.append(product_item)

    def checkout(self):
        self.basket = []


