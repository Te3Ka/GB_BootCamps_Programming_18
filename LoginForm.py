from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired

class LogForm(FlaskForm):
	name = StringField("Имя", validators=[DataRequired()])
	email = EmailField("Почта", validators=[DataRequired()])
	password = PasswordField("Пароль", validators=[DataRequired()])
	password_repeat = PasswordField("Повтор пароля", validators=[DataRequired()])
	remember_me = BooleanField("Запомни меня")
	submit = SubmitField("Зарегестрироваться")