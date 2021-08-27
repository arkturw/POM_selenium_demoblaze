class UserData:

    def __init__(self):
        self.name = 'test557788'
        self.password = 'Qwerty123456'

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def get_wrong_password(self):
        return 'abcdefgh'


class ProductData:

    def __init__(self):
        self.name = 'MacBook Pro'
        self.category = 'Laptops'

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category
