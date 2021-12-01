class Author():
    def __init__(self, name, surname, id = None):
        self.id = id
        self.name = name
        self.surname = surname

    def get_name(self):
        return f"{self.name} {self.surname}"