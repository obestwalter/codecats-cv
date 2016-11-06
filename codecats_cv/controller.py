import logging

from flask import Flask
from flask.templating import render_template

from codecats_cv.cnf import PATH, STATIC, SECRETS, data
from codecats_cv.model import get_experiences

log = logging.getLogger(__name__)

app = Flask(__name__, template_folder=PATH.VIEW, static_folder=PATH.STATIC)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = SECRETS.SECRET_KEY
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


# TODO use session and auth
class User:
    def __init__(self, name):
        self.name = name

    @property
    def isLoggedIn(self):
        return False


@app.context_processor
def inject_data_into_templates():
    return dict(STATIC=STATIC)


@app.route('/')
def index():
    return render_template(
        'main.html',
        MY=data.MY, experiences=get_experiences(), user=User('dohfie'))


@app.route('/add-entry', methods=['GET', 'POST'])
def add_entry():
    # TODO use WTFORMS
    # TODO check for post and add stuff from form
    return render_template('add-entry.html')


def run_devserver():
    logging.basicConfig(level=logging.DEBUG)
    app.config['DEBUG'] = True
    app.run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
    run_devserver()
