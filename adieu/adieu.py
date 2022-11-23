import inflect

p = inflect.engine()
friends = []

while True:
    try:
        item = input('Name: ')
        friends.append(item)
    except (EOFError, KeyError):
        break

print()
print('Adieu, adieu, to', p.join(friends))

