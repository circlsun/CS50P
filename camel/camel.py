name = list(input('camelCase: '))

for i in range(len(name)):
    if name[i].isupper():
        name[i] = "_" + name[i]
        print(name[i].lower(), end="")
    else:
        print(name[i], end="")
