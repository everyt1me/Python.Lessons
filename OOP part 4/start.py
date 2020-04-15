from lib.person import Users

user = Users("John", "Snow", "j_snow", "js@gmail.com", "john's_secret")
user.show_user_info()
user.save_user()
user2 = Users("Bran", "Stark", "b_stark", "bs@gmail.com", "doggy")
# user2.show_user_info()
user2.save_user()

users = user.show_all_users()
print(users)