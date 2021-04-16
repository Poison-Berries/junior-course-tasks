from os import environ
from sys import stderr

import flask


app = flask.Flask(__name__)



try:
    flags = [environ[f'flag{i}'] for i in range(7)]
except KeyError:
    print("Environment variables flag0, flag1, ..., flag6 must be set. Exiting", file=stderr)
    exit(1)



@app.route('/')
def index():
    return 'Добро пожаловать! Решите таски, расположенные на этом домене по адресам <a href="/0">/0</a>, <a href="/1">/1</a>, ..., <a href="/7">/7</a>'

@app.route('/0')
def one():
    if flask.request.args.get('get') == 'flag' and flask.request.args.get('flag') == 'get':
        return flags[0]
    else:
        return 'Чтобы получить флаг, отправьте GET запрос на эту страницу с параметрами get=flag и flag=get'

@app.route('/1', methods=['GET', 'POST'])
def two():
    if flask.request.method == 'POST' and flask.request.form.get('get') == 'flag' and flask.request.form.get('flag') == 'get':
        return flags[1]
    else:
        return 'Чтобы получить флаг, отправьте POST запрос на эту страницу с параметрами get=flag и flag=get'

@app.route('/2')
def three():
    if flask.request.headers.get('get') == 'flag' and flask.request.headers.get('flag') == 'get':
        return flags[2]
    else:
        return 'Чтобы получить флаг, отправьте GET запрос на эту страницу, с <b>http заголовками</b> get=flag и flag=get'

@app.route('/3')
def four():
    resp = flask.Response("Я уже отправил тебе флаг, просто возьми его")
    resp.headers['flag'] = flags[3]
    resp.headers['NEXT_TASK_HINT'] = "Y" + "E" * 1000 + "Y, your flag is above, you're cool, but finding flag for the NEXT task won't be so easy. The hint is: check my status (= response_code)!"
    return resp

@app.route('/4')
def five():
    return '', int(flags[4].replace('.', ''))

@app.route('/5')
def six():
    if flask.request.headers.get('Host') == 'GoOgLe.com':
        return flags[5]
    else:
        return 'Сложный таск<br><br>Вы зашли на ' + str(flask.request.headers.get('Host')) + ', чтобы получить флаг нужно зайти с GoOgLe.com (регистр важен)'

@app.route('/6', methods=['GET', 'POST'])
def seven():
    if flask.request.method == 'POST' and flask.request.form.get('teapot') == '418':
        return flags[6]
    else:
        return 'Сложный таск, придется погуглить<br><br>Чтобы получить флаг, отправьте POST запрос на эту страницу с параметром teapot, значением которого является число, которое я вернул бы тебе, если бы хотел сообщить, что я - чайник (teapot)'

@app.route('/7')
def eight():
    return 'Отлично! Таски закончились, если ты уже получил все флаги-<details><summary>[спойлер]</summary><div style="margin-left:30px;">даты</div></details>, то конвертируй их в имена старичков цтфа (имён должно быть 7, очевидно), затем отправьте этот список (в правильном порядке, разумеется) в telegram пользователю @kolayne, получи подтверждение - и это будет означать успешную сдачу зачета!'


if __name__ == "__main__":
    app.run('0.0.0.0', port=6202)
