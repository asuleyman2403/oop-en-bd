class InvalidEmailException(Exception):
    def __init__(self, email, message):
        self.email = email
        self.message = message
        super().__init__(message)


email = input('Enter your email:')

try:
    if len(email) < 5:
        error = InvalidEmailException(email, "Email is too short")

        # print('okokoko')
        # Exception will be raised only after this line under
        raise error
    if not (email.contains('@') or email.contains('.')):
        raise InvalidEmailException
except Exception as e:
    print(e.message)



