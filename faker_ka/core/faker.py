from faker_ka.generators.names import GeorgianNames


class Faker:
    def __init__(self):
        self.names = GeorgianNames()

    def first_name(self):
        return self.names.first_name()

    def last_name(self):
        return self.names.last_name()

    def full_name(self):
        return self.names.generate()

