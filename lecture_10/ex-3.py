a = int(input('Enter a number: '))
b = int(input('Enter second number: '))
try:
    print(a / b)
# This will handle any exception
except:
    print('Undefined exception')
    print(e)

try:
    print(a / b)
# This will handle any exception, print exact error
except Exception as e:
    print('Undefined exception')
    print(e, type(e))
