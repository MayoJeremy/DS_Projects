from shortener.db_man import Dbman
from random import randint
import config as cfg


class Url:
    def __init__(
        self,
        domain_name,
        original_url,
        short_url,
        user_id,
        url_id=0,
    ) -> None:

        self.url_id = url_id
        self.domain_name = domain_name
        self.original_url = original_url
        self.short_url = short_url
        self.user_id = user_id

        self.db = Dbman()

    def __repr__(self) -> str:
        return f"{self.short_url}"

    @staticmethod
    def get_list_of_urls_from_db() -> list:
        """Retrive URLs Data from DB.

        Returns:
            list: URL Data in Tuple.
        """
        sql = "SELECT * FROM url"
        sql_urls = Dbman().get_all_entries(sql)
        return sql_urls

    @staticmethod
    def make_list_of_urls_from_db_tuple(urls_list_from_db: list) -> list:
        """Generating URL Objects and creating List of them.

        Args:
            urls_list_from_db (list): URL List from DB

        Returns:
            list: List of URL Objects.
        """
        urls = []
        for db_url in urls_list_from_db:
            urls.append(
                Url(
                    db_url[1],
                    db_url[2],
                    db_url[3],
                    db_url[4],
                    db_url[0],
                )
            )
        return urls

    @classmethod
    def create_new_url_via_original_url_and_page_code(
        cls, original_url, page_code, user_id
    ):
        """Alternative initializer method if strings are not yet formatted.

        Args:
            original_url (_type_): URL from Userinput.
            page_code (_type_): Generated unique code for webpage
            user_id (_type_): UserID of logged in User

        Returns:
            _type_: URL Object
        """
        domain_name = Url.make_domain_name(original_url)
        short_url = Url.generate_short_url(page_code)

        return Url(domain_name, original_url, short_url, user_id)

    @staticmethod
    def generate_short_url(page_code: str) -> str:
        """Makes string out of Baseurl and pagecode

        Args:
            page_code (str): 5 Digit Code

        Returns:
            str: shortened url
        """

        return cfg.BASE_URL + "/" + page_code

    @staticmethod
    def make_domain_name(in_url: str) -> str:
        """Generates Domainname out of URL.

        Args:
            in_url (str): URL to extract Domain from.

        Returns:
            str: Domain
        """
        # Cut the Protocol prefix
        domain_name = in_url.split("//")[1]
        # Cut the name of Webpage
        domain_name = domain_name.split("/")[0]
        # Cut Domainpre-/suffix
        # domain_name = domain_name.split(".")[-2]

        return domain_name

    def save_to_db(self):
        """
        Saves this Instance to Database and sets url_id attribute accordingly.
        """

        sql = """INSERT INTO url (DomainName, OriginalUrL, ShortUrL, UserID)
        VALUES (%s,%s,%s,%s)
        """

        self.db.save_to_db(
            sql,
            (
                self.domain_name,
                self.original_url,
                self.short_url,
                self.user_id,
            ),
        )
        self.url_id = self.db.cursor.lastrowid

    @staticmethod
    def generate_page_code(urls_list: list) -> str:
        """Generates randomized 5 Letter string
        and checks if db has short url with page_code

        Args:
            urls_list (list): list to search uniqueness in

        Returns:
            str: with base_url concatenated string
        """
        while True:
            page_code = "".join(str(randint(0, 9)) for _ in range(cfg.PAGE_CODE_LEN))
            unique = True
            for url in urls_list:
                if Url.generate_short_url(page_code) == url.short_url:
                    unique = False
            if unique:
                return page_code
