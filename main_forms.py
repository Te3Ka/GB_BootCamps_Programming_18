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
		pass
	return render_template('registration.html', title="Регистрация", form=form)

if __name__ == '__main__':
	app.run()