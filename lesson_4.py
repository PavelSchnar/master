from utils import currency_rates
import sys

command = sys.argv[1]

if command == 'USD':
    print(currency_rates('usd'))

elif command == 'EUR':
    print(currency_rates('eur'))

elif command == 'GBP':
    print(currency_rates('gbp'))
