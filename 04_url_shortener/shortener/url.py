from shortener.db_man import Dbman


class Url:
    base_url = "https://wbs.com"

    def __init__(self, domain_name, original_url, short_url, user, url_id=0) -> None:
        self.url_id = url_id
        self.domain_name = domain_name
        self.original_url = original_url
        self.short_url = Url.base_url + "/" + short_url
        self.user = user

        self.db = Dbman()

    def __repr__(self) -> str:
        return f"{self.short_url}"

    @staticmethod
    def get_original_url_from_short_url(short_url: str):
        sql = """
            SELECT OriginalUrl
            FROM url
            WHERE ShortUrL = %s
        """

        return Dbman().get_one_entry(sql, short_url)

    @classmethod
    def create_new_url_via_input(cls, short_url, user):
        original_url = input("Url to shorten >> ")
        domain_name = original_url.split("//")[1].split("/")[0].split(".")[-2]
        if domain_name.startswith("www."):
            domain_name = domain_name[4:]
        return Url(domain_name, original_url, short_url, user)
