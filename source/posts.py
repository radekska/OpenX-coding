from collections import namedtuple


class Posts:
    def __init__(self, post_data_json):
        self.post_data_json = post_data_json
        self.Post = namedtuple('Post', list(self.post_data_json[0].keys()))

    def __iter__(self):
        return self.posts_iterator()

    def posts_iterator(self):
        for row in self.post_data_json:
            yield self.Post(*row.values())
