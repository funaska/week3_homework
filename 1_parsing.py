# Получение данных
# На сайте портала открытых данных Москвы есть таблица с популярными именами новорожденных. Напишите функцию, которая получает данные при помощи requests и читает содержимое в формате json. Для получения данных используйте ссылку http://api.data.mos.ru/v1/datasets/2009/rows

import requests
from secret_api_key import secret_api_key
import json
import ast

# print(secret_api_key)
data = requests.request('get', 'https://apidata.mos.ru/v1/datasets/2009/rows?api_key=' + secret_api_key)
text_data = data.text[1:-1]
# json_data = json.dumps(text_data)
json_data = ast.literal_eval(text_data)
# assert type(json_data) is dict

print(json_data)

# print(json_data)
# for rownum, peoples in enumerate(json_data):
#     print(peoples)
#     if rownum >= 10:
#         break
