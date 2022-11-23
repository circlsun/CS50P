import sys
import csv
from tabulate import tabulate


def main():
    check_arg()

    try:
        with open(sys.argv[1], 'r') as file:
            rows = csv.reader(file)
            headers = next(csv.reader(file))
            print(tabulate(rows, headers, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit('File does not exist')

def check_arg():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if '.csv' not in sys.argv[1]:
        sys.exit('Not a CSV file')


if __name__ == "__main__":
    main()

