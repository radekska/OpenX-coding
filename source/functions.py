# coding=utf-8
import json
import requests
from geopy.distance import distance


def get_data():
    post_data = requests.get("https://jsonplaceholder.typicode.com/posts")
    user_data = requests.get("https://jsonplaceholder.typicode.com/users")

    if post_data.status_code == 404 or user_data.status_code == 404:
        return ("""Could not connect to requested destination, check your internet connection...
    Error code: 404""")

    post_data_json = json.loads(post_data.text)
    user_data_json = json.loads(user_data.text)

    return user_data_json, post_data_json


def count_posts(user_post_data):
    return [f"{unp.User.name} napisał(a) {len(unp.Posts)} postów." for unp
            in user_post_data]


def check_unique_title(user_post_data):
    title_dict = dict()
    for unp in user_post_data:
        for post in unp.Posts:
            if post.title not in title_dict:
                title_dict[post.title] = 1
            else:
                title_dict[post.title] += 1

    return [key for key, value in title_dict.items() if value > 1]


def find_closest(user_post_data):
    closest_user_dict = dict()
    for unp_1 in user_post_data:
        distance_list = list()
        user_1_cords = tuple(unp_1.User.address['geo'].values())
        for unp_2 in user_post_data:
            if unp_1.User.name != unp_2.User.name:
                user_2_cords = tuple(unp_2.User.address['geo'].values())
                distance_ = distance(user_1_cords, user_2_cords)
                distance_list.append((round(distance_.kilometers), unp_2.User.name))
        closest_user_dict[unp_1.User.name] = min(distance_list)
    return closest_user_dict
