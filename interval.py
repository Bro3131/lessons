class Interval:
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b

    def __repr__(self):
        return f'interval[{self.a1},{self.b1}]'


def test_init():
    assert repr(Interval(1, 2)) == 'interval[1,2]'
