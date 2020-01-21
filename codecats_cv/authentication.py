from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class User(UserMixin):
    user_database = {"MaxMuster": ("MaxMuster", "Max")}

    def __init__(self, username, password):
        self.id = username
        self.password = password

    @classmethod
    def get(cls, id_):
        return cls.user_database.get(id_)


class LoginForm(FlaskForm):
    password = StringField("password", validators=[DataRequired()])

    def validate(self):
        return self.password.data == "rumpelstielzchen"
