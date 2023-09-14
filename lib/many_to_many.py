class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        self._contracts.append(new_contract)
        return new_contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)

    def contracts(self):
        return self._contracts.copy()


class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []

    def authors(self):
        return [contract.author for contract in self._contracts]

    def contracts(self):
        return self._contracts.copy()


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        self.author._contracts.append(self)
        self.book._contracts.append(self)
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all_contracts, key=lambda contract: contract.date)

