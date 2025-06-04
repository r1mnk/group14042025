from human import Human


class Student(Human):

    def __init__(
        self, gender: str, age: int, first_name: str, last_name: str, record_book: str
    ) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} {self.record_book}"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.record_book == other.record_book

    def __hash__(self):
        return hash(self.record_book)
