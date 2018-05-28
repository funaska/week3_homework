# Получение данных
# На сайте портала открытых данных Москвы есть таблица с популярными именами новорожденных. Напишите функцию, которая получает данные при помощи requests и читает содержимое в формате json. Для получения данных используйте ссылку http://api.data.mos.ru/v1/datasets/2009/rows

import requests
from secret_api_key import secret_api_key

# print(secret_api_key)
data = requests.request('get','https://apidata.mos.ru/v1/datasets/2009/rows?api_key=' + secret_api_key)
# json_data = data.json
text_data = data.text

print(json_data)
