from enum import Enum
from users.customer import Customer
import os
import time


class SystemState(Enum):
    INITIAL = 'INITIAL'
    LOGIN = 'LOGIN'
    REGISTER = 'REGISTER'
    REGISTER_AS_CUSTOMER = 'REGISTER_AS_CUSTOMER'
    REGISTER_AS_SELLER = 'REGISTER_AS_SELLER'
    SHOW_CATEGORIES_LIST = 'SHOW_CATEGORIES_LIST'
    EXIT = 'EXIT'


class System:
    # Static fields
    current_user = None
    current_state = SystemState.INITIAL
    categories = []
    customers = []
    sellers = []
    products = []
    super_admin = None
    is_running = True

    def __init__(self):
        pass

    def run(self):
        while System.is_running:
            match System.current_state:
                case SystemState.INITIAL:
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
                case SystemState.LOGIN:
                    os.system('cls')
                    print('Please enter your username and password: ')
                    data = input()
                    credentials = data.split(' ')
                    username = credentials[0]
                    password = credentials[1]
                    print(username, password)
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
                            System.current_state = SystemState.SHOW_CATEGORIES_LIST
                        else:
                            print('User is not found, please try again')
                            time.sleep(3)
                    else:
                        print('Invalid credentials, please try again')
                        time.sleep(4)
                case SystemState.REGISTER:
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
                case SystemState.REGISTER_AS_CUSTOMER:
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
                        customer = Customer(username, email, password)
                        System.customers.append(customer)
                        System.current_state = SystemState.LOGIN
                    else:
                        print('Invalid credentials, please try again')
                        time.sleep(4)
                case SystemState.SHOW_CATEGORIES_LIST:
                    print('HERE should be all categories list')
                    time.sleep(3)
                case SystemState.EXIT:
                    os.system('cls')
                    print('Bye')
                    System.is_running = False

