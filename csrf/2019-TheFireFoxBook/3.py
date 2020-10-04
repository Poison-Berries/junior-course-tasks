from threading import Lock
from hashlib import sha224

import flask

from common import solvers, solvers_mutex, \
    set_host_port_task, register_user_decorator, \
    confirmation_header, get_admin_csrf_token, \
    admin_csrf_token_mutex
from common import app


host = '0.0.0.0'
port = 8893
set_host_port_task(host, port, 3)


usernames = {} # From user_id to username
usernames_mutex = Lock()


calc_hash = lambda x: sha224(x.encode('utf-8')).hexdigest()


@app.route('/3', methods=['GET', 'POST'])
@register_user_decorator
def one():
    if flask.request.method == 'POST':
        with usernames_mutex:
            usernames[flask.request.cookies['user_id']] = flask.request.form['username']
    elif flask.request.cookies['user_id'] not in usernames.keys():
        return '<form method="POST"><p>Необходимо зарегистрироваться. Внимание! Крайне рекомендуем сделать ваше имя пользователя вашими именем и фамилией или какой-то кличкой или чем-то подобным, на английском языке, одним словом, но где имена собственные будут начинаиться с заглавных букв. Например, если вас зовут Никола Игрек, рекомендуем выбрать в качестве ника NikolaIgrek</p><p><input name="username" placeholder="Имя пользователя"></p><p><input type="submit" value="Зарегистрироваться"></p></form>'

    if solvers.get(flask.request.cookies.get('user_id'), False):
        return 'Вокруг начала играть музыка. Она то приближалась, то отдалялась, но в какой-то момент начала играть как будто в твоей голове. Ты пытался оглядываться, чтобы найти источник, но вокруг видел только черноту. За всем этим последовала яркая вспышка<br><br>Глава прочитана'
    return flask.render_template('3.html')

@app.route('/hack_3', methods=['GET', 'POST'])
def hack_one():
    if flask.request.method == 'GET':
        return f'<form method="POST"><input name="user_id"><input type="hidden" name="csrf_token" value="{calc_hash(usernames[flask.request.cookies["user_id"]])}"></form>'

    if flask.request.form.get('csrf_token') != calc_hash('FireFox'):
        return 'CSRF attack'

    if flask.request.headers.get(confirmation_header) != get_admin_csrf_token():
        return 'Вновь над мертвой водой поднимается пар'

    with solvers_mutex:
        solvers[flask.request.form['user_id']] = True
    return 'Success'


if __name__ == "__main__":
    app.run(host, port)
