from um import count


def main():
    test_default()


def test_default():
    assert count(r'Um, thanks for the album.') == 1
    assert count(r'Um, thanks, um...') == 2


if __name__ == "__main__":
    main()
