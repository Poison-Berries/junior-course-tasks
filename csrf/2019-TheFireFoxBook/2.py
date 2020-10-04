import flask

from common import solvers, solvers_mutex, \
    set_host_port_task, register_user_decorator, \
    confirmation_header, get_admin_csrf_token, \
    admin_csrf_token_mutex
from common import app


host = '0.0.0.0'
port = 8892
set_host_port_task(host, port, 2)


@app.route('/2')
@register_user_decorator
def one():
    if solvers.get(flask.request.cookies.get('user_id'), False):
        return 'Звонкий треск раздался за твой спиной. Ты обернулся и увидел не меньше сотни деревьев, высаженных плотной стеной. Ты обернулся обратно и понял, что оказался окружен деревьями. Из коры потёк сок. Ты поднял глаза туда, где должно было быть небо<br><br>Глава прочитана'
    return flask.render_template('2.html')

@app.route('/hack_2', methods=['GET', 'POST'])
def hack_one():
    if flask.request.method == 'GET':
        return '<form method="POST"><input name="user_id"></form>'

    if flask.request.headers.get(confirmation_header) != get_admin_csrf_token():
        return 'Скажи, зачем у крокодила есть слезы'

    with solvers_mutex:
        solvers[flask.request.form['user_id']] = True
    return 'Success'


if __name__ == "__main__":
    app.run(host, port)
