from plates import is_valid


def main():
    test_start()
    test_length()
    test_numbers()
    test_zero()
    test_punc()


def test_start():
    assert is_valid('ABCDEF') is True
    assert is_valid('1ABCDE') is False
    assert is_valid('A3CDEF') is False
    assert is_valid('63CDEF') is False


def test_length():
    assert is_valid('ABCDEF') is True
    assert is_valid('ABCDE') is True
    assert is_valid('ABC') is True
    assert is_valid('AB') is True
    assert is_valid('A') is False


def test_numbers():
    assert is_valid('ABC123') is True
    assert is_valid('ABCD12') is True
    assert is_valid('ABCDE1') is True
    assert is_valid('AB23EF') is False
    assert is_valid('ABC23F') is False
    assert is_valid("AA") is True
    assert is_valid("2A") is False
    assert is_valid("22") is False
    assert is_valid(" 2") is False


def test_zero():
    assert is_valid('ABC102') is True
    assert is_valid('CS50') is True
    assert is_valid('ABC012') is False
    assert is_valid('ABCD01') is False


def test_punc():
    assert is_valid('ABC,23') is False
    assert is_valid('ABC 23') is False
    assert is_valid('ABC.12') is False
    assert is_valid('AB:12') is False
    assert is_valid('AB/45') is False


if __name__ == "__main__":
    main()
