from hashlib import sha3_512
from random import random
from threading import Lock
from time import sleep
from functools import wraps
import atexit

import flask
from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from browsermobproxy import Server


def generate_id() -> str:
    """Generates a random id for an entity
    Returns:
        str: random hash
    """
    return sha3_512(str(random()).encode('utf-8')).hexdigest()


confirmation_header = 'X-really-the-fire-fox'
admin_csrf_token = generate_id()
admin_csrf_token_mutex = Lock()


host = None
port = None
task = None

options = None

browsermobproxy_server = None
proxy = None


def _init():
    global options, browsermobproxy_server, proxy

    options = webdriver.FirefoxOptions()
    options.set_headless()

    browsermobproxy_server = Server()
    browsermobproxy_server.start()
    atexit.register(lambda: browsermobproxy_server.stop())
    proxy = browsermobproxy_server.create_proxy()

    if task != 4:
        @app.after_request
        def add_header(response):
            response.headers['X-Frame-Options'] = 'DENY'
            return response

def set_host_port_task(host_, port_, task_):
    global host, port, task
    host = host_
    port = port_
    task = task_
    _init()

def get_admin_csrf_token():
    global admin_csrf_token
    return admin_csrf_token


solvers = {} # From user_id to `True` if task is solved
solvers_mutex = Lock()
fox_requests = {} # From request_id to request_text
fox_requests_mutex = Lock()


app = flask.Flask(generate_id())

def register_user_decorator(func):
    @wraps(func)
    def ans(*args, **kwargs):
        user_id = flask.request.cookies.get('user_id', generate_id())
        resp = flask.make_response(func(*args, **kwargs))
        resp.set_cookie('user_id', user_id)
        return resp
    return ans

@app.route('/')
@register_user_decorator
def index():
    return flask.render_template('0.html')

@app.route('/get_request/<request_id>')
def get_request(request_id):
    return fox_requests[request_id]


@app.route('/fox_request', methods=['POST'])
def fire_help():
    global admin_csrf_token

    request_id = generate_id()
    with fox_requests_mutex:
        fox_requests[request_id] = flask.request.form['message']

    profile = webdriver.FirefoxProfile()
    profile.set_proxy(proxy.selenium_proxy())
    if task == 1:
        # No idea what this is
        profile.set_preference("browser.download.folderList", 2)
        # Disable javascript
        profile.set_preference("javascript.enabled", False)

    with admin_csrf_token_mutex:
        admin_csrf_token = generate_id()
        proxy.headers({confirmation_header: admin_csrf_token})
        browser = webdriver.Firefox(firefox_options=options, firefox_profile=profile)
        if task == 4:
            # Set cookie:
            browser.get(f'http://{host}:{port}')
        # Without slash between port and get_admin_cookie_url
        browser.get(f'http://{host}:{port}/get_request/{request_id}')
        sleep(1)
    browser.quit()

    return 'Огненная Лисица прочитала твое обращение. Вернись назад и <b>обнови страницу</b>'
