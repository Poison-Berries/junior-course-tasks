from threading import Lock

import flask

from common import solvers, solvers_mutex, \
    set_host_port_task, register_user_decorator, \
    confirmation_header, get_admin_csrf_token, \
    admin_csrf_token_mutex, generate_id
from common import app


host = '0.0.0.0'
port = 8894
set_host_port_task(host, port, 4)


csrf_tokens = {}
csrf_tokens_mutex = Lock()


@app.route('/4')
@register_user_decorator
def one():
    solve_type = solvers.get(flask.request.cookies.get('user_id'), 0)
    if solve_type:
        return flask.render_template('run_out.html', flag=('GingerBread{' + ('Vakhinak' if solve_type == 1 else 'Veronika') + '_wants_to_help_you}'))
    return flask.render_template('4.html')

def hack_one_common():
    user_id = flask.request.cookies['user_id']

    # Ensure a token exists
    with csrf_tokens_mutex:
        csrf_tokens[user_id] = csrf_tokens.get(user_id, generate_id())

    if flask.request.method == 'GET':
        return f'<form method="POST"><input name="user_id"><input type="hidden" name="csrf_token" value="{csrf_tokens[user_id]}"></form>'

    # Remember token before update
    token = csrf_tokens[user_id]
    # If it's not a get request, change token
    with csrf_tokens_mutex:
        csrf_tokens[user_id] = generate_id()

    if token != flask.request.form['csrf_token']:
        return 'CSRF attack'

    if flask.request.headers.get(confirmation_header) != get_admin_csrf_token():
        return 'Я подонок, я гнида, мне на все наплевать'


@app.route('/hack_4', methods=['GET', 'POST'])
def hack_one():
    ans = hack_one_common()
    if ans is not None:
        return ans

    with solvers_mutex:
        solvers[flask.request.form['user_id']] = 1
    return 'Success'

@app.route('/do_hack_4', methods=['GET', 'POST'])
def do_hack_one():
    ans = hack_one_common()
    if ans is not None:
        return ans

    with solvers_mutex:
        solvers[flask.request.form['user_id']] = 2
    return 'Success'


if __name__ == "__main__":
    app.run(host, port)
