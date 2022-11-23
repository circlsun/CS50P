import sys

list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        inn = input('Date: ')
        month, day, year = inn.replace('"', '').strip().split('/')
        if (0 < int(month) < 11) and (1 < int(day) < 31) and (1000 < int(year) < 2999):
            print(f'{year}-{int(month):02}-{int(day):02}')
            sys.exit(0)
        else:
            continue
    except (ValueError, IndexError, AttributeError):
        try:
            monthday, year = inn.split(',')
            year = year.replace(' ', '')
            month, day = monthday.split()
            for i in list:
                if month == i:
                    month = list.index(i) + 1
            if 1 < int(day) < 31 and 1000 < int(year) < 2999:
                print(f'{year}-{int(month):02}-{int(day):02}')
                sys.exit(0)
        except (ValueError, IndexError, AttributeError):
            continue
