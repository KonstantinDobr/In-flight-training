from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index//<title>')
def index(title="Заготовка"):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof.lower())


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
