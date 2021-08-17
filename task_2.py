import requests
from requests import utils



def currency_rates(val):

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encode = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encode)
    val = val.upper()
    result = content.find(val)
    result_2 = content[result:].find('<Value>')
    return (content[result + result_2 + 7:result + result_2 + 14])

print(currency_rates('EUR'))
print(currency_rates('usd'))
