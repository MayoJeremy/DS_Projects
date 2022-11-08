"""
Application to shorten an URL and
save URL to shorten and generated URL to Database
"""
from shortener.user import User
from shortener.url import Url


def get_mode() -> int:
    """
    Prompts user to input desired Mode via integer. Loops
    until viable Mode is selected and returns Mode.

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
            print(f"{url.domain_name} | {url.short_url} | {user.user_name}")


def url_lookup_mode(urls: list) -> None:
    """Prompts User for shortened URL
    and iterates over list of URLs and checks
    for original URL

    Args:
        urls (list): List of URLs in DB
    """
    short_url = input("Shorturl >> ")
    for url in urls:
        if short_url == url.short_url:
            print(url.original_url)


def main():
    user = User.user_login()
    mode = get_mode()
    db_urls_list = Url.get_list_of_urls_from_db()
    urls_list = Url.make_list_of_urls(db_urls_list)
    print()

    if mode == 1:
        url_creation_mode(user, urls_list)
    elif mode == 2:
        url_display_mode(user, urls_list)
    elif mode == 3:
        url_lookup_mode(urls_list)


if __name__ == "__main__":
    main()
