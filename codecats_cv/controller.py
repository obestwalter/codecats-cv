import logging

from flask import Flask
from flask.templating import render_template

from codecats_cv.cnf import PATH, STATIC, SECRETS, data

log = logging.getLogger(__name__)

app = Flask(__name__, template_folder=PATH.VIEW, static_folder=PATH.STATIC)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = SECRETS.SECRET_KEY


@app.context_processor
def inject_data_into_templates():
    return dict(STATIC=STATIC)


@app.route('/')
def index():
    return render_template('main.html', MY=data.MY)


@app.route('/add-entry', methods=['GET', 'POST'])
def add_entry():
    # TODO use WTFORMS
    # TODO check for post and add stuff from form
    return render_template('add-entry.html')


def run_devserver():
    logging.basicConfig(level=logging.DEBUG)
    app.config['DEBUG'] = True
    app.run(port=5000, debug=True)


if __name__ == '__main__':
    run_devserver()
