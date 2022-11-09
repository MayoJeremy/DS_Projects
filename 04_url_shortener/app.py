"""
Application to shorten an URL
"""
from shortener.user import User
from shortener.url import Url
import config as cfg


def get_mode() -> int:
    """
    Prompts user to input desired Mode via integer. Loops
    until viable Mode is selected and returns Mode.

    Returns:
        int: Selected Mode

    """
    print("\nMainmenu")
    while True:
        mode = input(
            """(1) Create new URL
(2) List all URLs
(3) Find URL from shortened URL
(0) Exit
>> """
        )
        try:
            mode = int(mode)
        except ValueError:
            print("Please put in an Integer\n")
        else:
            # TODO modeselections from config
            if mode in [0, 1, 2, 3]:
                return mode
            print("Invalid Mode selected. Try again\n")


def url_creation_mode(user: User, urls: list) -> None:
    """Prompts User to input unshortened URL and
    shortens it. Calls Functions to create URL Object
    and save it to DB.

    Args:
        user (User): Instance of logged in User
        urls (list): List of URLs in DB
    """
    original_url = input("Url to shorten >> ")
    page_code = Url.generate_page_code(urls)
    new_url = Url.create_new_url_via_original_url_and_page_code(
        original_url,
        page_code,
        user.user_id,
    )
    new_url.save_to_db()


def url_display_mode(user: User, urls: list) -> None:
    """Prints formatted String of every saved URL a
    User previously registered

    Args:
        user (User): Instance of logged in User
        urls (list): List of URLs in DB
    """
    for url in urls:
        if url.user_id == user.user_id:
            print(f"{url.domain_name} | {url} | {user}")


def url_lookup_mode(urls: list) -> None:
    """Prompts User for shortened URL
    and iterates over list of URLs and checks
    for original URL

    Args:
        urls (list): List of URLs in DB
    """
    user_in = input("Shorturl >> ")

    if user_in.isdigit() and len(user_in) == cfg.PAGE_CODE_LEN:
        user_in = Url.generate_short_url(user_in)

    for url in urls:
        if user_in == url.short_url:
            print(f"Original URL = {url.original_url}")
            return

    print(f"No Entry for Shorturl {user_in} found")


def main():
    user = User.user_login()
    mode = get_mode()
    while mode:
        db_urls_list = Url.get_list_of_urls_from_db()
        urls_list = Url.make_list_of_urls_from_db_tuple(db_urls_list)
        print()

        if mode == 1:
            url_creation_mode(user, urls_list)
        elif mode == 2:
            url_display_mode(user, urls_list)
        elif mode == 3:
            url_lookup_mode(urls_list)
        mode = get_mode()


if __name__ == "__main__":
    main()
