from shortener.db_man import Dbman
from random import randint
import config as cfg


class Url:
    base_url = cfg.BASE_URL

    def __init__(self, domain_name, original_url, short_url, user_id, url_id=0) -> None:
        self.url_id = url_id
        self.domain_name = domain_name
        self.original_url = original_url
        self.short_url = short_url
        self.user_id = user_id

        self.db = Dbman()

    def __repr__(self) -> str:
        return f"{self.short_url}"

    @staticmethod
    def get_list_of_urls():
        sql = "SELECT * FROM url"
        sql_urls = Dbman().get_all_entries(sql)
        urls = []
        for sql_url in sql_urls:
            urls.append(
                Url(
                    sql_url[1],
                    sql_url[2],
                    sql_url[3],
                    sql_url[4],
                    sql_url[0],
                )
            )
        return urls

    @classmethod
    def create_new_url_via_input(cls, page_code, user):
        original_url = input("Url to shorten >> ")
        domain_name = original_url.split("//")[1].split("/")[0].split(".")[-2]
        if domain_name.startswith("www."):
            domain_name = domain_name[4:]
        short_url = cls.base_url + "/" + page_code
        return Url(domain_name, original_url, short_url, user)

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
    def generate_page_code(urls_list: list):
        while True:
            new_short_url = "".join(str(randint(0, 9)) for _ in range(5))
            unique = True
            for url in urls_list:
                if Url.base_url + "/" + new_short_url == url.short_url:
                    unique = False
            if unique:
                return new_short_url
