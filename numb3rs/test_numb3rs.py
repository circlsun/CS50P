from numb3rs import validate

def main():
    test_val()
    test_val_false()

def test_val_true():
    assert validate(r'1.2.3.4') == True
    assert validate(r'127.0.0') == False

def test_val_false():
    assert validate(r'255.255.255.255') == True
    assert validate(r'512.2.3.1') == False
    assert validate(r'cat') == False
    assert validate(r'1.1.1.512') == False



if __name__ == "__main__":
    main()