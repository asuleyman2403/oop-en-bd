

class Category:
    def __init__(self, category_id, name):
        self._id = category_id
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_id(self):
        return self._id

    def set_id(self, category_id):
        self._id = category_id
