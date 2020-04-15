if __name__ == "__main__":
    Users


class Users:
    def __init__(self, first_name, last_name, username, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__email = email
        self.__password = password

    def show_user_info(self):
        print("First name: ", self.__first_name, "\nLast name: ", self.__last_name,
              "\nUsername: ", self.__username, "\nEmail: ", self.__email, "\nPassword: ******")

    def save_user(self):

        f = open('db.txt', 'a')
        f.write(self.__first_name + "#" + self.__last_name + "#" +
                self.__username + "#" + self.__email + "#" + self.__password + "#\n")
        f.close()

    def show_all_users(self):
        users = []
        with open('db.txt') as db_file:
            for line in db_file:
                if len(line.strip()) > 0:
                    item = line.strip()
                    items = item.split("#")
                    users.append(items)
        return users

    # user = []
    # user.append(self.__first_name)
    # user.append(self.__last_name)
    # user.append(self.__username)
    # user.append(self.__email)
    # user.append(self.__password)
    # with open('db.txt', 'w') as db_file:
    #     db_file.write(users[0])
