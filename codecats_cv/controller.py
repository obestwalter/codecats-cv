from flask import Flask
from flask.templating import render_template

from codecats_cv.cnf import PATH, STATIC

app = Flask(__name__, template_folder=PATH.VIEW, static_folder=PATH.STATIC)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = "secret key (not really)"


@app.context_processor
def inject_dict_for_all_templates():
    return dict(STATIC=STATIC)


@app.route('/')
def index():
    return render_template('index.html')


def run_devserver():
    # log.info("serving on http://localhost:%s", 5000)
    app.config['DEBUG'] = True
    app.run(port=5000, debug=True)


if __name__ == '__main__':
    run_devserver()
