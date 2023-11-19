from enum import Enum
from users.customer import Customer
from users.user import UserRole
from users.seller import Seller
from shop.product import ProductItem
import os
import time


class SystemState(Enum):
    INITIAL = 'INITIAL'
    LOGIN = 'LOGIN'
    REGISTER = 'REGISTER'
    REGISTER_AS_CUSTOMER = 'REGISTER_AS_CUSTOMER'
    REGISTER_AS_SELLER = 'REGISTER_AS_SELLER'
    SELLER_MENU = 'SELLER_MENU'
    SHOW_SELLER_PRODUCT_ITEMS = 'SHOW_SELLER_PRODUCT_ITEMS'
    ADD_NEW_PRODUCT_ITEM = 'ADD_NEW_PRODUCT_ITEM'
    DELETE_PRODUCT_ITEM = 'DELETE_PRODUCT_ITEM'
    ADMIN_MENU = 'ADMIN_MENU'
    CUSTOMER_MENU = 'CUSTOMER_MENU'
    SHOW_CATEGORIES_LIST = 'SHOW_CATEGORIES_LIST'
    SHOW_CATEGORY_PRODUCTS = 'SHOW_CATEGORY_PRODUCTS'
    SHOW_CUSTOMERS_BASKET = 'SHOW_CUSTOMERS_BASKET'
    LOGOUT = 'LOGOUT'
    EXIT = 'EXIT'


class System:
    # Static fields
    current_user = None
    current_state = SystemState.INITIAL
    selected_category = None
    categories = []
    products = []
    customers = []
    sellers = []
    super_admin = None
    is_running = True

    def __init__(self):
        pass

    def show_initial_state(self):
        os.system('cls')
        print('Hello, user!')
        print('Please, choose one of the following actions:')
        print('(1) Sign in to the system')
        print('(2) Sign up to the system')
        action_type = input()
        if action_type == '1':
            System.current_state = SystemState.LOGIN
        elif action_type == '2':
            System.current_state = SystemState.REGISTER
        else:
            System.current_state = SystemState.EXIT

    def show_login(self):
        os.system('cls')
        print('Please enter your username and password: ')
        data = input()
        credentials = data.split(' ')
        username = credentials[0]
        password = credentials[1]
        if len(username) and len(password):
            current_user = None
            for customer in System.customers:
                if customer.get_username() == username \
                        and customer.get_password() == password:
                    current_user = customer
                    break
            for seller in System.sellers:
                if seller.get_username() == username \
                        and seller.get_password() == password:
                    current_user = seller
                    break
            if current_user:
                System.current_user = current_user
                if current_user.get_role() == UserRole.SELLER:
                    System.current_state = SystemState.SELLER_MENU
                elif current_user.get_role() == UserRole.SUPER_ADMIN:
                    System.current_state = SystemState.ADMIN_MENU
                else:
                    System.current_state = SystemState.CUSTOMER_MENU
            else:
                print('User is not found, please try again')
                time.sleep(3)
        else:
            print('Invalid credentials, please try again')
            time.sleep(4)

    def show_signup(self):
        os.system('cls')
        print('Please choose how you want to be registered to the system:')
        print('(1) As customer')
        print('(2) As seller')
        print('(3) Exit')
        action_type = input()
        if action_type == '1':
            System.current_state = SystemState.REGISTER_AS_CUSTOMER
        elif action_type == '2':
            System.current_state = SystemState.REGISTER_AS_SELLER
        else:
            System.current_state = SystemState.EXIT

    def handle_signup(self, is_seller):
        os.system('cls')
        print('Please enter your email, username, password split by single empty space')
        data = input()
        credentials = data.split(' ')
        # TODO: handle null pointer exception
        email = credentials[0]
        username = credentials[1]
        password = credentials[2]
        # TODO: add proper validation for credentials
        if len(email) and len(username) and len(password):
            print(credentials)
            if is_seller:
                seller = Seller(username, email, password, [])
                System.sellers.append(seller)
                System.current_state = SystemState.LOGIN
            else:
                customer = Customer(username, email, password, [])
                System.customers.append(customer)
                System.current_state = SystemState.LOGIN
        else:
            print('Invalid credentials, please try again')
            time.sleep(4)

    def show_seller_menu(self):
        os.system('cls')
        print('Choose following actions: ')
        print('(1) Show product items')
        print('(2) Add product item')
        print('(3) Delete product item')
        print('(4) Logout')
        action = input()
        if action == '1':
            System.current_state = SystemState.SHOW_SELLER_PRODUCT_ITEMS
        elif action == '2':
            System.current_state = SystemState.ADD_NEW_PRODUCT_ITEM
        elif action == '3':
            System.current_state = SystemState.DELETE_PRODUCT_ITEM
        else:
            System.current_state = SystemState.LOGOUT

    def add_product_item(self):
        os.system('cls')
        print('Creating product item...')
        categories = System.categories
        for category in categories:
            print(category)
        category_id = input('Choose category id: \n')
        current_category = None
        for category in categories:
            if int(category_id) == category.get_id():
                current_category = category
                break
        category_products = []
        for product in System.products:
            if product.category_id == current_category.get_id():
                category_products.append(product)
        for product in category_products:
            print(product)
        product_id = input('Choose product id: \n')
        current_product = None
        for product in category_products:
            if int(product_id) == product.get_id():
                current_product = product
                break
        count = input('Type product count:\n')
        price = input('Set product price:\n')
        product_item = ProductItem(current_product, int(count), int(price))
        print('Product item is successfully')
        print(product_item)
        time.sleep(3)
        if System.current_user and System.current_user.get_role() == UserRole.SELLER:
            System.current_user.add_product_item(product_item)
        System.current_state = SystemState.SELLER_MENU

    def show_seller_product_items(self):
        os.system('cls')
        for item in System.current_user.product_items:
            print(item)
        action = input('Press enter to return to menu: \n')
        System.current_state = SystemState.SELLER_MENU

    def show_customer_menu(self):
        os.system('cls')
        print('Choose following actions: ')
        print('(1) Show categories list')
        print('(2) See my basket')
        print('(3) Logout')
        action = input()
        if action == '1':
            System.current_state = SystemState.SHOW_CATEGORIES_LIST
        elif action == '2':
            System.current_state = SystemState.SHOW_CUSTOMERS_BASKET
        else:
            System.current_state = SystemState.LOGOUT

    def show_categories_list(self):
        os.system('cls')
        print('Here is available product categories: ')
        for category in System.categories:
            print(category)
        category_id = input('Select category or press any: \n')
        current_category = None
        for category in System.categories:
            if int(category_id) == category.get_id():
                current_category = category
                break
        if current_category:
            System.selected_category = current_category
            System.current_state = SystemState.SHOW_CATEGORY_PRODUCTS
        else:
            System.current_state = SystemState.CUSTOMER_MENU

    def show_category_products(self):
        category = System.selected_category
        matching_products = []
        for seller in System.sellers:
            for item in seller.product_items:
                if item.get_product().category_id == category.get_id():
                    matching_products.append(item)

            if len(matching_products):
                print(f'##### {seller.get_username()} ######')
                for item in matching_products:
                    print(item)
        product_item_id = input('Enter product id: \n')
        selected_product = None
        for product in matching_products:
            if product.get_id() == int(product_item_id):
                selected_product = product
                break
        if selected_product:
            System.current_user.add_product_to_basket(selected_product)
            System.current_state = SystemState.SHOW_CUSTOMERS_BASKET
        else:
            System.current_state = SystemState.CUSTOMER_MENU

    def show_basket(self):
        print('Here is you basket')
        for product in System.current_user.basket:
            print(product)
        print('Choose following actions: ')
        print('(1) Checkout')
        print('(2) Go back to menu')
        action = input()
        if action == '1':
            System.current_user.basket = []
            os.system('cls')
            print('You have successfully checked out your products')
            time.sleep(2)
        System.current_state = SystemState.CUSTOMER_MENU

    def run(self):
        while System.is_running:
            match System.current_state:
                case SystemState.INITIAL:
                    self.show_initial_state()
                case SystemState.LOGIN:
                    self.show_login()
                case SystemState.REGISTER:
                    self.show_signup()
                case SystemState.REGISTER_AS_CUSTOMER:
                    self.handle_signup(False)
                case SystemState.REGISTER_AS_SELLER:
                    self.handle_signup(True)
                case SystemState.SELLER_MENU:
                    self.show_seller_menu()
                case SystemState.ADD_NEW_PRODUCT_ITEM:
                    self.add_product_item()
                case SystemState.SHOW_SELLER_PRODUCT_ITEMS:
                    self.show_seller_product_items()
                case SystemState.CUSTOMER_MENU:
                    self.show_customer_menu()
                case SystemState.SHOW_CATEGORIES_LIST:
                    self.show_categories_list()
                case SystemState.SHOW_CATEGORY_PRODUCTS:
                    self.show_category_products()
                case SystemState.SHOW_CUSTOMERS_BASKET:
                    self.show_basket()
                case SystemState.LOGOUT:
                    self.current_user = None
                    self.selected_category = None
                    System.current_state = SystemState.INITIAL
                case SystemState.EXIT:
                    os.system('cls')
                    print('Bye')
                    System.is_running = False

