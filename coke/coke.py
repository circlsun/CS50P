res  =  50
coins  =  [5, 10, 25, 50]
n = 0

while True:
    print('Amount due: ', res)
    n = int(input('Insert Coin: '))

    if n in coins:
        res -=n

        if res <=  0:
            print('Change owed: ', abs(res))
            break