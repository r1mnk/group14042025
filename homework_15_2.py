class Fraction:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def __mul__(self, other: "Fraction") -> "Fraction":
        num = self.a * other.a
        den = self.b * other.b
        return Fraction(num, den)

    def __add__(self, other: "Fraction") -> "Fraction":
        num = self.a * other.b + other.a * self.b
        den = self.b * other.b
        return Fraction(num, den)

    def __sub__(self, other: "Fraction") -> "Fraction":
        num = self.a * other.b - other.a * self.b
        den = self.b * other.b
        return Fraction(num, den)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b == self.b * other.a

    def __gt__(self, other: "Fraction") -> bool:
        return self.a * other.b > self.b * other.a

    def __lt__(self, other: "Fraction") -> bool:
        return self.a * other.b < self.b * other.a

    def __str__(self) -> str:
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == "Fraction: 21, 18"
f_d = f_b * f_a
assert str(f_d) == "Fraction: 6, 18"
f_e = f_a - f_b
assert str(f_e) == "Fraction: 3, 18"

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print("OK")
