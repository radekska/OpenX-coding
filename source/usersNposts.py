from .users import Users
from .posts import Posts
from collections import namedtuple


class UsersnPosts:
    def __init__(self, data_json):
        self.user_data_json, self.post_data_json = data_json
        self.u_data = list(Users(self.user_data_json))
        self.p_data = list(Posts(self.post_data_json))
        self.UsernPost = namedtuple('UsernPost', ['User', 'Posts'])

    def __iter__(self):
        return self.up_iterator()

    def up_iterator(self):
        posts = list()
        for user in self.u_data:
            for post in self.p_data:
                if user.id == post.userId:
                    posts.append(post)
            yield self.UsernPost(user, posts)
            posts = []
