import pytest


class MultiInterval:
    def __init__(self, *args):
        # todo: check arguments type
        def type_check(b):
            for i in b:
                if type(i) == list and len(i) == 2:
                    for j in i:
                        if type(j) == int:
                            continue
                        else:
                            raise RuntimeError('bro u got wrong types')
                else:
                    raise RuntimeError('bro u got wrong types')
        self.a = args
        # if type_check(args) is not None:
        type_check(args)

    def norm(self):
        if len(self.a) >= 2:
            args = sorted(list(self.a))
            r = []
            # for i, j in zip(range(len(args))[:-1], range(len(args))[1:]):
            #     if args[i][1] >= args[j][0]:
            #         r.append([args[i][0], args[j][1]])
            #     else:
            #         r = r + [args[i], args[j]]
            _1 = args[0]
            for _2 in args[1:]:
                if _1[0] == _1[1] and _2[0] == _2[1] and _2[0] - _1[0] == 1:
                    _1 = [_1[0], _2[0]]
                elif _1[1] - _1[0] > 0 and _2[0] == _2[1] and _2[1] - _1[1] == 1:
                    _1 = [_1[0], _2[1]]
                elif _1[0] == _2[0]:
                    _1 = _2
                elif _1[1] >= _2[1]:
                    pass
                elif _1[1] >= _2[0] and _1[0] < _2[1]:
                    _1 = [_1[0], _2[1]]
                else:
                    if _1 not in r:
                        r.append(_1)
                        _1 = _2
            self.a = r + ([_1] if _1 not in r else [])
        else:
            self.a = list(self.a)
        # else:
        #     self.a = []

    def __repr__(self):
        return f'{self.a}'

    def __eq__(self, other):
        return self.a == other

    def __and__(self, other):
        def get_intersection(interval1, interval2):
            new_min = max(interval1[0], interval2[0])
            new_max = min(interval1[1], interval2[1])
            return [new_min, new_max] if new_min <= new_max else None
        other = [x for x in (get_intersection(y, z) for y in self.a for z in other.a) if x is not None]
        return other


def test_wrong_input():
    with pytest.raises(RuntimeError):
        MultiInterval([2, 4], 'no')


def test_wrong_input2():
    with pytest.raises(RuntimeError):
        MultiInterval([2, 4], [2, 6], 1)


def test_correct_input():
    assert repr(MultiInterval([1, 2], [3, 4], [5, 6])) == '[[1, 2], [3, 4], [5, 6]]'


def test_init_empty():
    assert repr(MultiInterval()) == '[]'


def test_init_single():
    assert repr(MultiInterval([0, 1])) == '[[0, 1]]'


def test_init_double_non_intersecting():
    assert repr(MultiInterval([0, 1], [2, 3])) == '[[0, 1], [2, 3]]'


def test_init_double_include():
    assert repr(MultiInterval([0, 2], [0, 1])) == '[[0, 2]]'


def test_init_double_intersecting():
    assert repr(MultiInterval([0, 1], [1, 3])) == '[[0, 3]]'


def test_init_triple_intersect_include():
    assert repr(MultiInterval([0, 1], [2, 3], [0, 4])) == '[[0, 4]]'


def test_init_triple_intersect():
    assert repr(MultiInterval([0, 2], [1, 3], [2, 4])) == '[[0, 4]]'


def test_init_triple_dot():
    assert repr(MultiInterval([0, 0], [1, 1], [2, 2])) == '[[0, 2]]'


def test_init_triple_include():
    assert repr(MultiInterval([0, 1], [0, 2], [0, 3])) == '[[0, 3]]'


def test_init_triple_include1():
    assert repr(MultiInterval([0, 1], [-1, 2], [-1, 100500])) == '[[-1, 100500]]'


def test_init():
    assert repr(MultiInterval([1, 2], [9, 9], [100, 100], [200, 300])) == '[[1, 2], [9, 9], [100, 100], [200, 300]]'


def test_and():
    assert MultiInterval((MultiInterval([0, 2], [5, 10], [13, 23], [24, 25]) & MultiInterval([1, 5], [8, 12], [15, 24]))) == MultiInterval([1, 2], [5, 5], [8, 10], [15, 23], [24, 24])


def test_and2():
    assert MultiInterval(*(MultiInterval([0, 2], [3, 4], [5, 6], [7, 8]) & MultiInterval([2, 3], [4, 5], [6, 7], [8, 9]))) == MultiInterval([2, 8])


def test_and3():
    assert MultiInterval([0, 1], [2, 3], [4, 5], [6, 7]) & MultiInterval([8, 9], [10, 11], [12, 13], [14, 15]) == MultiInterval()


def test_and4():
    assert MultiInterval() & MultiInterval() == MultiInterval()


def test_test():
    assert MultiInterval([0, 2], [1, 3], [0, 3])
