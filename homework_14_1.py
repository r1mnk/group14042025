class Human:

    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.gender}, {self.age}, {self.first_name}, {self.last_name}"


class Group:

    def __init__(self, number: str) -> None:
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        if len(self.group) >= 10:
            raise TooManyStudentsError()
        self.group.add(student)

    def delete_student(self, last_name: str) -> None | str:
        student = self.find_student(last_name)
        try:
            self.group.remove(student)
        except KeyError:
            print(f"########## User {last_name} not found#######")

    def find_student(self, last_name: str) -> Student | None:
        for student in set(self.group):
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Number:{self.number}\n {all_students} "


class TooManyStudentsError(Exception):
    def __init__(self, message="У групі не може бути більше 10 студентів"):
        super().__init__(message)


st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
st2 = Student("Female", 25, "Liza", "Taylor", "AN145")
st3 = Student("Male", 22, "Jim", "Beam", "RB003")
st4 = Student("Female", 23, "Lara", "Croft", "RB004")
st5 = Student("Male", 24, "Bruce", "Wayne", "RB005")
st6 = Student("Female", 25, "Diana", "Prince", "RB006")
st7 = Student("Male", 26, "Clark", "Kent", "RB007")
st8 = Student("Female", 27, "Natasha", "Romanoff", "RB008")
st9 = Student("Male", 28, "Tony", "Stark", "RB009")
st10 = Student("Female", 29, "Wanda", "Maximoff", "RB010")
st11 = Student("Male", 30, "Steve", "Jobs", "RB011")
st12 = Student("Male", 30, "Tester", "Testerenko", "RB012")

students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]

gr = Group("PD1")

for s in students:
    try:
        gr.add_student(s)
        print(f"Added {s}")
    except TooManyStudentsError:
        print(f"Not added {s}")

assert str(gr.find_student("Jobs")) == str(st1), "Test1"
assert gr.find_student("Jobs2") is None, "Test2"
assert (
    isinstance(gr.find_student("Jobs"), Student) is True
), "Метод поиска должен возвращать экземпляр"
