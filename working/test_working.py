from working import convert
import pytest

def main():

    test_time()
    test_convert_no_minute()
    test_convert_empty()
    test_wrong_format()
    test_wrong_hour()
    test_wrong_minute()
    test_invalid_time_format()
    test_final()

def test_time():
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def test_convert_no_minute():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5:00 PM') == '09:00 to 17:00'

def test_convert_empty():
    with pytest.raises(ValueError):
        assert convert("")

def test_wrong_format():
    with pytest.raises(ValueError):
        assert convert('9 AM - 5 PM')

def test_wrong_hour():
    with pytest.raises(ValueError):
       assert convert('13 PM to 17 PM')
       assert convert('9:50 AM to 13:00 PM')
       assert convert('19:50 AM to 12:00 AM')

def test_wrong_minute():
    with pytest.raises(ValueError):
       assert convert('9:60 AM - 9:60 PM')
       assert convert('9:60 AM to 12:00 PM')
       assert convert('9:00 AM to 12:90 PM')

def test_invalid_time_format():
    with pytest.raises(ValueError):
       assert convert('12:60 AM - 13:00 PM')
       assert convert('9 - 5')
       assert convert('9 AM - 5 PM')
       assert convert('9 AM - 9 PM')
       assert convert('09:00 AM - 17:00 PM')
       assert convert('09:00 am - 17:00 PM')
       assert convert('00:00 AM - 7:00 PM')
       assert convert("9-00 AM to 5-00 PM")

def test_final():
    with pytest.raises(ValueError):
        convert('8:70 AM to 12:70 PM')
    with pytest.raises(ValueError):
        convert('9AM to 8PM')
    with pytest.raises(ValueError):
        convert('9:00 AM to 17:00')
    with pytest.raises(ValueError):
        convert('9 AM - 8 PM')
    with pytest.raises(ValueError):
        convert('9:00 AM to 17:00 PM')

if __name__ == "__main__":
    main()