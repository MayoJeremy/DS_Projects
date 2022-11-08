"""
Application to shorten an URL and
save URL to shorten and generated URL to Database
"""
from shortener.db_man import Dbman
from shortener.user import User
from shortener.url import Url

DBX = Dbman()


def user_login() -> User:

    """
    Prompts user to input username and passwort. Loops
    until Login successful and Userobject created.

    Returns:
        User: Logged in Userobject
    """

    print("Loginmask!\n")
    while True:
        username = input("Username >> ")
        password = input("Password >> ")
        user_id = DBX.get_user_id_from_db(username, password)
        if user_id:
            return User(user_id, username, password)
        else:
            print("Wrong credentials. Try again\n")


def get_mode() -> int:
    """
    Prompts user to input desired Mode via integer. Loops
    until viable Mode is selected

    Returns:
        int: Selected Mode

    """
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


def new_url(user: User):
    """Generates new Url Object

    Args:
        user (User): Logged in User
    """
    print("New URL")
    short_url = DBX.get_new_random_short_url()
    new_url = Url.create_new_url_via_input(short_url, user)
    print(new_url)
    url_id = DBX.save_url_to_db_and_get_url_id(new_url)
    new_url.url_id = url_id


def main():
    user = user_login()
    mode = get_mode()
    print()
    if mode == 1:
        new_url(user)
    elif mode == 2:
        for saved_url in user.get_all_saved_urls():
            print("{} | {} | {}".format(*saved_url))
    elif mode == 3:
        short_url = input("Shorturl >> ")
        print(Url.get_original_url_from_short_url((short_url,)))


if __name__ == "__main__":
    main()
