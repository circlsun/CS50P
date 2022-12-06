def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:2].isdigit() and (2 <= len(s) <= 6) and s.isalnum():
        for i in range(len(s)):
            if s[i].isdigit():
                if not s[i:].isdigit():
                    return False
                elif s[i] == '0':
                    return False
                else:
                    return True
            elif s.isalpha():
                return True
    return False


if __name__ == "__main__":
    main()
