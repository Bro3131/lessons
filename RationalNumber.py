def euclid_algorithm(a, b):
    c = a % b
    while c:
        a = b
        b = c
        c = a % b
    return b


class RationalNumber:
    def __init__(self, arg1=0, arg2=1):
        self.arg1 = arg1
        self.arg2 = arg2
        pass

    def __repr__(self):
        return f'{self.arg1}/{self.arg2}'

    def __eq__(self, other):
        gcd1 = euclid_algorithm(self.arg1, self.arg2)
        gcd2 = euclid_algorithm(other.arg1, other.arg2)
        numerator1, denominator1 = self.arg1 // gcd1, self.arg2 // gcd1
        numerator2, denominator2 = other.arg1 // gcd2, other.arg2 // gcd2

        return (numerator1, denominator1) == (numerator2, denominator2)

    def __add__(self, second_number):
        return RationalNumber((self.arg1 * second_number.arg2 + second_number.arg1 * self.arg2),
                              (second_number.arg2 * self.arg2))

    def __sub__(self, second_number):
        return RationalNumber((self.arg1 * second_number.arg2 - second_number.arg1 * self.arg2),
                              (second_number.arg2 * self.arg2))

    def __mul__(self, second_number):
        return RationalNumber((self.arg1 * second_number.arg1), (self.arg2 * second_number.arg2))

    def __truediv__(self, second_number):
        return RationalNumber((self.arg1 * second_number.arg2), (self.arg2 * second_number.arg1))

    def __lt__(self, other):
        first = self.arg1 * other.arg2
        second = other.arg1 * self.arg2
        return first <= second

    def __le__(self, other):
        first = self.arg1 * other.arg2
        second = other.arg1 * self.arg2
        return first <= second


def test_equality_unnormalized():
    a1 = RationalNumber(1, 2)
    a2 = RationalNumber(2, 4)
    assert a1 == a2


def test_equality():
    assert RationalNumber() == RationalNumber(0, 1)


def test_rational_repr():
    assert repr(RationalNumber(4, 5)) == '4/5'


def test_rational_default():
    assert repr(RationalNumber()) == '0/1'


def test_add_check_result():
    a1 = RationalNumber(3, 4)
    a2 = RationalNumber(5, 8)
    assert type(a1 + a2) == RationalNumber and a1 + a2 == RationalNumber(44, 32)


def test_sub_check_result():
    a1 = RationalNumber(5, 6)
    a2 = RationalNumber(7, 12)
    assert type(a1 - a2) == RationalNumber and a1 - a2 == RationalNumber(3, 12)


def test_mul_check_result():
    a1 = RationalNumber(3, 4)
    a2 = RationalNumber(5, 7)
    assert type(a1 * a2) == RationalNumber and a1 * a2 == RationalNumber(15, 28)


def test_truediv_check_result():
    a1 = RationalNumber(3, 5)
    a2 = RationalNumber(4, 9)
    assert type(a1 / a2) == RationalNumber and a1 / a2 == RationalNumber(27, 20)


def test_lt_diff_denominators():
    a1 = RationalNumber(3, 7)
    a2 = RationalNumber(1, 2)
    assert type(a1 < a2) == bool and a1 < a2


def test_le_check_result():
    a1 = RationalNumber(5, 5)
    a2 = RationalNumber(9, 9)
    assert type(a1 <= a2) == bool and a1 <= a2


def test_gt_check_result():
    a1 = RationalNumber(5, 8)
    a2 = RationalNumber(4, 9)
    assert type(a1 > a2) == bool and a1 > a2


def test_ge_check_result():
    a1 = RationalNumber(10, 10)
    a2 = RationalNumber(3, 3)
    assert type(a1 >= a2) == bool and a1 >= a2

