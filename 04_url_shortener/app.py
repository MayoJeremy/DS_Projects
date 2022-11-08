"""
Application to shorten an URL and
save URL to shorten and generated URL to Database
"""
from shortener.user import User
from shortener.url import Url


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


def url_creation_mode(user: User, urls: list) -> None:
    original_url = input("Url to shorten >> ")
    page_code = Url.generate_page_code(urls)
    new_url = Url.create_new_url_via_input(original_url, page_code, user.user_id)
    new_url.save_to_db()


def url_display_mode(user: User, urls: list) -> None:
    for url in urls:
        if url.user_id == user.user_id:
            print(f"{url.domain_name} | {url.short_url} | {user.user_name}")


def main():
    user = User.user_login()
    mode = get_mode()
    urls = Url.get_list_of_urls()
    print()

    if mode == 1:
        url_creation_mode(user, urls)
    elif mode == 2:
        url_display_mode(user, urls)
    elif mode == 3:
        short_url = input("Shorturl >> ")
        for url in urls:
            if short_url == url.short_url:
                print(url.original_url)


if __name__ == "__main__":
    main()
