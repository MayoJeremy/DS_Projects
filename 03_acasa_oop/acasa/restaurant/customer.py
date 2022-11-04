class Customer:
    def __init__(self, first_name, last_name, tel, customer_id=0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.customer_id = customer_id

    def __repr__(self) -> str:
        return f"{self.first_name}, {self.last_name}\nTel: {self.tel}\nKNr {self.customer_id}"
