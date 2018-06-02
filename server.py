from flask import Flask
from parsing import parsing_mos_ru

app = Flask(__name__)

@app.route('/')
def index():
    json_stuff = parsing_mos_ru()
    return json_stuff
    # return '''<table>
    # <tr>
    #     <th>Заголовок колонки 1</th>
    #     <th>Заголовок колонки 2</th>
    #     <th>Заголовок колонки 3</th>
    # </tr>
    # <tr>
    #     <td>Данные 1</td>
    #     <td>Данные 2</td>
    #     <td>Данные 3</td>
    # </tr>
    # </table>'''


if __name__ == '__main__':
    app.run()
