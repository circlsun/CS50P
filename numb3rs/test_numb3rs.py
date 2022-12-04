from numb3rs import validate


def main():
    test_val_false()
    test_val_true()


def test_val_true():
    assert validate(r'1.2.3.4') is True
    assert validate(r'127.0.0') is False


def test_val_false():
    assert validate(r'255.255.255.255') is True
    assert validate(r'512.2.3.1') is False
    assert validate(r'cat') is False
    assert validate(r'1.1.1.512') is False


if __name__ == "__main__":
    main()
