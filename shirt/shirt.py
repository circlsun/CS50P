import sys
from PIL import Image, ImageOps
import glob, os
from os.path import splitext

def main():
    check_arg()
    try:
        size = (600, 600)

        shirt = Image.open('shirt.png')
        before = Image.open(sys.argv[1]) #sourse

        new_picture = ImageOps.fit(before, size)
        new_picture.paste(shirt, shirt)
        new_picture.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')

def check_arg():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if check_ex(file1[1]) == False:
        sys.exit('Invalid output')
    if check_ex(file2[1]) == False:
        sys.exit('Invalid output')
    if file1[1].lower() != file2[1].lower():
        sys.exit('Input and output have different extensions')

def check_ex(file):
    if file in ['.jpg', 'jepg', '.png']:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
