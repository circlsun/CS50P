from random import randint

while True:
    try:
        level = int(input("Level: "))
        n = randint(1, level)
        break
    except (ValueError, IndexError, NameError):
        continue


while True:
    try:
        res = int(input("Guess: "))

        if res < n:
            print("Too small!")
        elif res > n:
            print("Too large!")
        else:
            print("Just right!")
            break
    except (ValueError, IndexError, NameError):
        pass