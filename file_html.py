from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
	with open('file.txt', 'r', encoding='utf-8') as file:
		resultData = list()
		for line in file.readlines():
			resultData.append(tuple(line.split('\n')[0].split(';')))

	return render_template('main.html', data=resultData)

if __name__ == '__main__':
	app.run()