class Person:
    people_count = 0

    def __init__(self, name, surname, age):
        self.full_name = name + " " + surname



person = Person("Bayurzhan", "Sukymbek", 19)
print(person.full_name)




