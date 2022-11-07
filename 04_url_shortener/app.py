"""
Application to shorten an URL and
save URL to shorten and generated URL to Database
"""
from shortener.db_man import Dbman
from shortener.user import User

DBX = Dbman()


def userLogin() -> User:
    print("Loginmask!\n")
    while True:
        username = input("Username >> ")
        password = input("Password >> ")
        user_id = DBX.get_user_id_from_db(username, password)
        if user_id:
            return User(user_id, username, password)
        else:
            print("Wrong credentials. Try again\n")


def getMode():
    print("Mainmenu")
    while True:
        mode = int(
            input(
                """
(1) Create new URL
(2) List all URLs
(3) Find URL from shortened URL
>> """
            )
        )
        if mode in [1, 2, 3]:
            return mode
        print("Invalid Mode selected. Try again\n")


def main():
    user = userLogin()
    mode = getMode()


if __name__ == "__main__":
    main()
