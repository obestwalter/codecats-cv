import logging
import os

from flask import Flask, render_template, url_for, redirect, request
from flask_login import LoginManager, login_required

from codecats_cv.authentication import LoginForm, User
from codecats_cv.cnf import PATH, STATIC, SECRETS, data
from codecats_cv.model import get_experiences

log = logging.getLogger(__name__)

app = Flask(__name__, template_folder=PATH.VIEW, static_folder=PATH.STATIC)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = SECRETS.SECRET_KEY
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id_):
    return User.get(id_)


@app.context_processor
def inject_data_into_templates():
    return dict(STATIC=STATIC)


@app.route("/login", methods=["GET", "POST"])
def login():
    # WARNING not implemented yet
    form = LoginForm()
    if form.validate_on_submit():
        # [load the user from the database]
        # [check that their password is valid]
        # login_user(user)
        # flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))

    return render_template("login.html", form=form)


@app.route('/')
def index():
    return render_template(
        'main.html', MY=data.MY, experiences=get_experiences())


@app.route('/add-entry', methods=['GET', 'POST'])
@login_required
def add_entry():
    # WARNING not implemented yet
    return render_template('add-entry.html')


def run_devserver():
    logging.basicConfig(level=logging.DEBUG)
    os.environ['WERKZEUG_DEBUG_PIN'] = 'off'
    app.config.update(
        TEMPLATES_AUTO_RELOAD=True,
        DEBUG=True
    )
    app.run(port=8080)


if __name__ == '__main__':
    run_devserver()
