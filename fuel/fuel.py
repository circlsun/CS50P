def main():
    fraction = input('Fraction: ')
    percentage = convert(fraction)
    if gauge(percentage) == 'F' or gauge(percentage) == 'E':
        print(gauge(percentage))
    else:
        print(convert(fraction), '%', sep='')


def convert(fraction):
    while True:
        try:
            n = fraction.split('/')
            x, y = int(n[0]), int(n[1])

            if x <= y:
                res = (x / y) * 100
                return round(res)
            else:
                continue

        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'


if __name__ == "__main__":
    main()