class MultiInterval:
    def __init__(self, *args):
        self.a = list(args)

    def __repr__(self):
        return f'{self.a}'

    def __eq__(self, other):
        return self.a == other

    def __and__(self, other):
        def get_intersection(interval1, interval2):
            new_min = max(interval1[0], interval2[0])
            new_max = min(interval1[1], interval2[1])
            return [new_min, new_max] if new_min <= new_max else None
        return [x for x in (get_intersection(y, z) for y in self.a for z in other.a) if x is not None]

def test_init():
    assert repr(MultiInterval([1, 2], [9, 9], [100, 100], [200, 300])) == '[[1, 2], [9, 9], [100, 100], [200, 300]]'


def test_and():
    assert MultiInterval([0, 2], [5, 10], [13, 23], [24, 25]) & MultiInterval([1, 5], [8, 12], [15, 24]) == MultiInterval([1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25])


def test_and2():
    assert MultiInterval([0, 2], [3, 4], [5, 6], [7, 8]) & MultiInterval([2, 3], [4, 5], [6, 7], [8, 9]) == MultiInterval([2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8])


def test_and3():
    assert MultiInterval([0, 1], [2, 3], [4, 5], [6, 7]) & MultiInterval([8, 9], [10, 11], [12, 13], [14, 15]) == MultiInterval()


def test_and4():
    assert MultiInterval() & MultiInterval() == MultiInterval()
