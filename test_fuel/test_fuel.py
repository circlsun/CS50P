import pytest
from fuel import convert
from fuel import gauge


def main():
    test1()
    test2()
    test3()
    test_zero()
    test_value()
    test_correct()


def test1():
    assert convert('1/2') == 50
    assert convert('1/4') == 25
    assert convert('3/4') == 75


def test2():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'


def test3():
    assert gauge(1) == 'E'
    assert gauge(0) == 'E'


def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_value():
    with pytest.raises(ValueError):
        convert('cat/dog')


def test_correct():
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'


if __name__ == '__main__':
    main()
