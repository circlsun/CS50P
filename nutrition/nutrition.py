key = input('Item: ').lower().capitalize()
table = {'Apple': 130, 'Avocado': 50, 'Banana': 110, 'Cantaloupe': 50, 'Grapefruit': 50,
'Grapes': 90, 'Honeydew Melon': 50, 'Kiwifruit': 90, 'Lemon': 15, 'Lime': 20, 'Nectatine': 60,
'Orange': 80, 'Peach': 60, 'Pear': 100, 'Pineapple': 50, 'Plums': 70, 'Strawberries': 50,
'Sweet cherries': 100, 'Tangerine': 50, 'Watermelon': 80}


if key in table:
    print(table[key])




