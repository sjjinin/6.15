from flask import Flask, render_template, request
from random import choice

web_site = Flask(__name__)



@web_site.route('/')
def index():
	return render_template('index.html')

# hello

@web_site.route('/user/', defaults={'username': None})
@web_site.route('/user/<username>')
def generate_user(username):
	if not username:
		username = request.args.get('username')

	if not username:
		return 'Sorry error something, malformed request.'

	return render_template('personal_user.html', user=username)


web_site.run(host='0.0.0.0', port=8080)