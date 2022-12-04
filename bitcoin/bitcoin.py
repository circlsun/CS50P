import sys
import requests

if len(sys.argv) == 2:
    try:
        usd = float(sys.argv[1])
    except IndexError:
        pass
else:
    print('Missing command-line argument')
    sys.exit(1)

try:
    URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(URL)
    data = response.json()
    course = data["bpi"]["USD"]["rate_float"]
    usdd = usd * course
except requests.RequestException:
    pass

print(f"${usdd:,.4f}")
