class RationalNumber:
    def __init__(self, arg1=0, arg2=1):
        self.arg1 = arg1
        self.arg2 = arg2
        pass

    def __repr__(self):
        return f'{self.arg1}/{self.arg2}'


def test_rational_repr():
    assert repr(RationalNumber(4, 5)) == '4/5'


def test_rational_default():
    assert repr(RationalNumber()) == '0/1'
