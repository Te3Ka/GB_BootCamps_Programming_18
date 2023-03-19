from flask import Flask, render_template
from LoginForm import LogForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MaX13PaynE'


@app.route('/')
def main():
	return render_template("main.html")

@app.route('/registration', methods=['GET', 'POST'])
def reg():
	form = LogForm()
	if form.validate_on_submit():
		if form.password_repeat.data != form.password.data:
			return render_template('registration.html', title="Регистрация", form=form, 
									message='Пароли не совпадают!')
		
		with open('file.txt', 'a', encoding='utf-8') as file:
			file.write(f'{form.name.data};{form.email.data};{form.password.data}\n')
		return render_template('registration.html', message='Всё верно')

	return render_template('registration.html', title="Регистрация", form=form)

if __name__ == '__main__':
	app.run()