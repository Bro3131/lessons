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