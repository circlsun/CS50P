def main():
    string = list(input('Input: '))
    print('Output:', shorten(string))


def shorten(string):
    new = []
    glss = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for i in range(len(string)):
        if string[i] not in glss:
            new.append(string[i])
            text = ''.join(new)
    return text


if __name__ == "__main__":
    main()
