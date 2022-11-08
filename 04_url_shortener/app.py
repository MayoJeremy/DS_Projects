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
        user_id = User.get_user_id_from_db(username, password)
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


def main():
    user = user_login()
    mode = get_mode()
    urls = Url.get_list_of_urls()
    print()

    if mode == 1:
        page_code = Url.generate_page_code(urls)
        new_url = Url.create_new_url_via_input(page_code, user.user_id)
        new_url.save_to_db()
    elif mode == 2:
        for url in urls:
            if url.user_id == user.user_id:
                print(f"{url.domain_name} | {url.short_url} | {user.user_name}")

    elif mode == 3:
        short_url = input("Shorturl >> ")
        for url in urls:
            if short_url == url.short_url:
                print(url.original_url)


if __name__ == "__main__":
    main()
