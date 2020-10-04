import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'Не рекомендуется продолжать просмотр, если вы не решили предыдущие таски. Чтобы продолжить, нажмите <a href="/5">сюда</a>'

@app.route('/5')
def five():
    return flask.render_template('5.html')

@app.route('/meta')
def meta():
    return flask.render_template('5_meta.html')


if __name__ == "__main__":
    app.run('0.0.0.0', 8895)
