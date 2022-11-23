import sys
import csv



def main():
    catalog = []
    check_arg()
    try:
        with open(sys.argv[1], "r") as file1:
            reader = csv.DictReader(file1)
            for row in reader:
                 split_name = row['name'].split(',')
                 catalog.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": row['house']})

        with open(sys.argv[2], "w") as file2:
            writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
            writer.writerow({"first": 'first', "last": 'last', "house": 'house'})
            for row in catalog:
                writer.writerow({"first": row['first'], "last": row['last'], "house": row['house']})

    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')


def check_arg():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if '.csv' not in sys.argv[1]:
        sys.exit('Not a CSV file')
    if ('.csv' not in sys.argv[1]) or ('.csv' not in sys.argv[2]) :
        sys.exit('Not a CSV file')



if __name__ == "__main__":
    main()
