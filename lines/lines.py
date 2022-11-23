import sys


def main():
    n = 0
    check_arg()

    try:
        file = open(sys.argv[1], 'r')
        lines = file.readlines()

    except FileNotFoundError:
        sys.exit('File does not exist')

    for line in lines:
        if check_line(line) == False:
            n +=1
    print(n)

def check_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False

def check_arg():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if '.py' not in sys.argv[1]:
        sys.exit('Not a Python file')



if __name__ == "__main__":
    main()





