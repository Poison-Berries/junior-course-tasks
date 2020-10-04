import flask

from common import solvers, solvers_mutex, \
    set_host_port_task, register_user_decorator, \
    confirmation_header, get_admin_csrf_token, \
    admin_csrf_token_mutex
from common import app


host = '0.0.0.0'
port = 8891
set_host_port_task(host, port, 1)


@app.route('/1')
@register_user_decorator
def one():
    if solvers.get(flask.request.cookies.get('user_id'), False):
        return 'Вокруг разразился грохот. Под тобой задрожала земля. Твои глаза закрылись, чтобы моргнуть<br><br>Глава прочитана'
    return flask.render_template('1.html')

@app.route('/hack_1')
def hack_one():
    if flask.request.headers.get(confirmation_header) != get_admin_csrf_token():
        return 'Your dad is 44 (fourty four)'

    with solvers_mutex:
        solvers[flask.request.args['user_id']] = True
    return 'Success'


if __name__ == "__main__":
    app.run(host, port)
