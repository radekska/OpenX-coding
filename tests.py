import unittest
from source import *

data_json = get_data()
user_post_iterator = UsersnPosts(data_json[0], data_json[1])


class TestPostsUsers(unittest.TestCase):
    def test_posts(self):
        """
        Test if posts iterator is being created properly by Posts class
        """
        posts_iterator = Posts(data_json[1])
        posts_list = list(posts_iterator)

        self.assertTrue(posts_list)
        self.assertEqual(len(posts_list), 100)

    def test_users(self):
        """
        Test if users iterator is being created properly by Users class
        """
        users_iterator = Posts(data_json[0])
        users_list = list(users_iterator)

        self.assertTrue(users_list)
        self.assertEqual(len(users_list), 10)

    def test_posts_users(self):
        """
        Test if posts - users iterator is being created properly by UsersnPosts class
        """
        posts_users_iterator = UsersnPosts(data_json[0], data_json[1])
        posts_users_list = list(posts_users_iterator)
        self.assertTrue(posts_users_list)
        self.assertEqual(len(posts_users_list), 10)


class TestFunctions(unittest.TestCase):
    def test_get_data(self):
        """
        Test if function can get data properly
        """
        self.assertTrue(get_data())
        self.assertIsInstance(get_data(), tuple)

    def test_count_posts(self):
        """
        Test if function can count posts per user properly
        """
        for unp in user_post_iterator:
            self.assertEqual(len(unp.Posts), 10)

    def test_check_unique_title(self):
        """
        Test if function finds not unique post titles
        """
        self.assertFalse(check_unique_title(user_post_iterator))

    def test_find_closest(self):
        """
        Test if function finds closest distances between users
        """
        correct_distance = (1810, 2841, 2841, 701, 862, 3786, 7619, 6738, 701,
                            862)
        distance_ = find_closest(user_post_iterator)
        distance_ = tuple(d for d, n in distance_.values())
        self.assertTupleEqual(correct_distance, distance_)


if __name__ == '__main__':
    unittest.main()
