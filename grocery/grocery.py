dict = {}

while True:
    try:
        key = input().upper()

        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1

    except (EOFError, KeyError):
        break

for i in sorted(dict.keys()):
    print(dict[i], i)