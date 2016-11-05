import logging

from flask import Flask
from flask.templating import render_template

from codecats_cv.cnf import PATH, STATIC, SECRETS

log = logging.getLogger(__name__)

try:
    from codecats_cv.secrets import DATA
except ImportError:
    DATA = tuple()
    log.warning("no secret data - using defaults")

secrets = SECRETS(*DATA)
app = Flask(__name__, template_folder=PATH.VIEW, static_folder=PATH.STATIC)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = secrets.SECRET_KEY


@app.context_processor
def inject_dict_for_all_templates():
    return dict(STATIC=STATIC)


@app.route('/')
def index():
    return render_template('index.html')


def run_devserver():
    logging.basicConfig(level=logging.DEBUG)
    app.config['DEBUG'] = True
    app.run(port=5000, debug=True)


if __name__ == '__main__':
    run_devserver()
