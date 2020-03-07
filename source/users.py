from collections import namedtuple


class Users:
    def __init__(self, user_data_json):
        self.user_data_json = user_data_json
        self.args = list(self.user_data_json[0].keys())
        self.User = namedtuple('User', self.args)

    def __iter__(self):
        return self.users_iterator()

    def users_iterator(self):
        for row in self.user_data_json:
            yield self.User(*row.values())
