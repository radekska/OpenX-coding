from source import *


if __name__ == '__main__':
	data_json = get_data()
	user_post_iterator = UsersnPosts(data_json)

	print("============= 1 - LICZBA POSTÓW ===================")
	print(count_posts(user_post_iterator), end='\n\n')

	print("=========== 2 - NIEUNIKALNE TYTUŁY POSTÓW ============")
	print(check_unique_title(user_post_iterator), "- Nie znaleziono nieunikalnych postów.", end='\n\n')

	print("============= 3 - NAJBLIŻSI UŻYTKOWNICY ====================")
	[print(f"{k} jest najbliżej {v[1]} ({v[0]} km)") for k, v in find_closest(user_post_iterator).items()]



