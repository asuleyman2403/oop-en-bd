map = {
    'key': 5
}


try:
    print(map['nonexistingkey'])
except KeyError:
    print('Key does not exist')
