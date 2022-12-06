import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    h1, h2, m1, m2 = None, None, None, None

    if matches := re.fullmatch(r'^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) \
                to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$', s):

        format1 = matches.group(4)
        format2 = matches.group(8)
        h1 = int(matches.group(2))
        h2 = int(matches.group(6))
        m1 = matches.group(3)
        m2 = matches.group(7)

        if h1 > 12 or h2 > 12:
            raise ValueError

        elif format1 == 'AM':
            if (h1 != 12) and (m1 is None or m2 is None):
                h2 = h2 + 12
                return f'{h1:02d}:00 to {h2:02d}:00'
            elif h1 == 12 and m1 is None or m2 is None:
                return f'{00:02d}:00 to {h2:02d}:00'
            else:
                if format2 == 'PM' and h1 != 12:
                    h2 = h2 + 12
                    return f'{h1:02d}:{int(m1):02} to {h2:02d}:{int(m2):02}'
                else:
                    return f'{00:02d}:{int(m1):02} to {h2:02d}:{int(m2):02}'

        elif format1 == 'PM':
            if (h2 != 12) and (m1 is None or m2 is None):
                h1 = h1 + 12
                return f'{h1:02d}:00 to {h2:02d}:00'
            elif (h2 == 12) and (m1 is None or m2 is None):
                return f'{h1:02d}:00 to {00:02d}:00'
            else:
                if format2 == 'AM' and h2 != 12:
                    h1 = h1 + 12
                    return f'{h1:02d}:{int(m1):02} to {h2:02d}:{int(m2):02}'
                else:
                    f'{h1:02d}:{int(m1):02} to {00:02d}:{int(m2):02}'

    else:
        raise ValueError


if __name__ == "__main__":
    main()
