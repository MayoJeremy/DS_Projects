class Url:
    base_url = "https://wbs.com"

    def __init__(self, domain_name, original_url, short_url, user_id, url_id=0) -> None:
        self.url_id = url_id
        self.domain_name = domain_name
        self.original_url = original_url
        self.short_url = short_url
        self.user_id = user_id

    def __repr__(self) -> str:
        return f"https://{self.domain_name}/{self.short_url}"

    @classmethod
    def create_new_url_via_input(cls, short_url, user_id):
        original_url = input("Url to shorten >> ").split("//")[1]
        domain_name = original_url.split("/")[0]
        return Url(domain_name, original_url, short_url, user_id)
