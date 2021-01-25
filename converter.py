import json
import requests

def converter(currency_input, amount, currency_output):
    """ Converter currencies from 
    currency in allowed_currency list to 
    another currency in this lis """

    allowed_currencies = ['BTC', 'BCC', 'LTC', 'ETH', 'ETC', 'XRP']
    data = requests.get('https://api.binance.com/api/v3/ticker/price?').json()

    # check if input data is allowed
    if currency_input in allowed_currencies and currency_output in allowed_currencies:
        if not (type(amount) is int or type(amount) is float):
            return "El monto a convertir debe ser un numero Real pero se recibio: {}".format(amount)

        symbol = currency_input + currency_output

        filter_obj = list(filter(lambda obj: obj['symbol'] == symbol, data))
        if filter_obj:
            price = filter_obj[0].get('price')
            resp = {
                'currencyInput': currency_input,
                'currencyOutput': currency_output,
                'amount': amount,
                'result': amount*float(price)
            }
            return json.dumps(resp)
        else:
            return "No se encontró factor de conversion de {} a {}".format(currency_input, currency_output)
    else:
        return "Las divisas permitidas son solo: {}".format(', '.join(allowed_currencies))


if __name__ == "__main__":
    print(converter("BCC", 100, "BTC"))