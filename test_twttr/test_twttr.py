from twttr import shorten


def main():
    test_default()
    test_default2()
    test_numbers()
    test_punct()


def test_default():
    assert shorten('hello, world') == "hll, wrld"


def test_default2():
    assert shorten('check50') == "chck50"
    assert shorten('TWITTER') == "TWTTR"
    assert shorten('TwItTeR') == "TwtTR"


def test_numbers():
    assert shorten('123456789') == "123456789"


def test_punct():
    assert shorten('!?.,') == "!?.,"


if __name__ == "__main__":
    main()
