import requests
import pprint
import json
import datetime as dt
from decimal import Decimal


def currency_rates(currency="USD"):
    if currency:
        currency = currency.upper()

    url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    response = requests.get(url)

    dict = json.loads(response.text)

    # pprint.pprint(dict['Valute'][currency]['Value'])
    # pprint.pprint(dict)

    # Проверка на наличие валюты в get()
    if currency not in dict['Valute']:
        return None

    start = dt.datetime.utcnow() + dt.timedelta(hours=3)
    rate = dict['Valute'][currency]['Value']

    # Пример с float
    return f"Курс {currency} на {start.strftime('%d.%m.%Y %H:%M:%S')} равен {float(rate)} руб"
