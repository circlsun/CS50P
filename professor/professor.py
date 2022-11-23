from random import randint

def main():
    score, err = 0, 0
    level = get_level()

    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)
        res = x + y
        sum = f'{str(x)} + {str(y)} = '
        print(sum, end='')

        try:
            if int(input()) == res:
                score +=1
            else:
                err +=1
                print('EEE')
                print(sum, end='')
                if int(input()) != res:
                    err +=1
                    print('EEE')
                    print(sum, end='')
                else:
                    continue
                if int(input()) != res:
                    err +=1
                    print('EEE')
                else:
                    continue
                if err >= 3:
                    print(sum + str(res))
        except (ValueError, IndexError, NameError):
            print('EEE')
            continue

    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level <= 3:
                return level
                break
            else:
                continue
        except (ValueError, IndexError, NameError):
            continue

def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    if level == 2:
        return randint(10, 99)
    if level == 3:
        return randint(100, 999)


if __name__ == "__main__":
    main()


