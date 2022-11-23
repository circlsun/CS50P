expressions = input('Expressions: ')
x, y, z = expressions.split(' ')

match y:
    case '+':
        print(float(x) + float(z))
    case '-':
        print(float(x) - float(z))
    case '/':
        print(float(x) / float(z))
    case '*':
        print(float(x) * float(z))
