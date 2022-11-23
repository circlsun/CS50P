from bank import value

def main():
    test_default()
    test_default2()
    test_default3()
    test_default4()

def test_default():
    assert value('hello') == 0

def test_default2():
    assert value('Hello, Newman') == 0

def test_default3():
    assert value('How you doing?') == 20
    assert value('Hey') == 20
    assert value('Hi') == 20


def test_default4():
    assert value("What's happening?") == 100
    assert value("good morning") == 100

    
if __name__ == "__main__":
    main()