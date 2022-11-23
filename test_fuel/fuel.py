def main():
    fraction = input('Fraction: ')
    fraction_conv = convert(fraction)
    out = gauge(fraction_conv)
    print(out)


def convert(fraction):
    while True:
        try:
            x, y = fraction.split('/')
            x1 = int(x)
            y1 = int(y)
            if x1 <= y1:
                res = int((x1 / y1) * 100)
                return res
            else:
                fraction = input('Fraction: ')
                pass
        except (ValueError,ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return str(percentage) + '%'


if __name__ == "__main__":
    main()