#!/Users/jeff/.pyenv/shims/python

import os
from flask import Flask, request

app = Flask(__name__)

def check_dir(directory):
	if os.path.isdir(directory):
		if directory.endswith('/'):
			pass
		else:
			directory += '/'
	return directory

@app.route('/')
def home():
	display_str = '<h1>Home page for solution.py. Visit either:<br><br></h1>' + \
				  'http://127.0.0.1:5000/scan?directory=DIRPATH<br><br>' + \
				  'OR<br><br>' + \
				  'http://127.0.0.1:5000/rescan?directory=DIRPATH<br><br>' + \
				  'where DIRPATH is diretory path such as: /Users/'
	return display_str


@app.route('/scan')
def scan():
	"""Scan function that scans the directory provided as an argument and create
	the hash database 'FileList' on disk"""
	directory = request.args['directory']
	directory = check_dir(directory)

	results_list = []
	if os.path.isdir(directory):
		for file in os.listdir(directory):
			file_path = os.path.join(directory, file)
			if os.path.isfile(file_path) and file != 'FileList':
				results_list.append(file_path)
		result = '<br>'.join(results_list)

	else:
		result = f'<h2>ERROR</h2><h3>{directory}<br><br> is NOT a directory.' \
				 '<h3>Please try again with a directory path that exists.</h3>'
	return result


@app.route('/rescan')
def rescan():
	"""Rescan function that loads pickled hash database from disk, called
	FileList"""
	directory = request.args['directory']
	directory = check_dir(directory)
	if os.path.isdir(directory):
		result = '<p>Rescanning the following directory using the pickled ' \
					 f'"FileList" file on disk:<br><br>{directory}</p>'
	else:
		result = f'<h2>ERROR</h2><h3>{directory}<br><br> is NOT a directory.' \
				 '<h3>Please try again with a directory path that exists.</h3>'
	return result


def main():
	"""Main function for web app"""
	app.run(debug=True, port=5000)

if __name__ == "__main__":
	app.run()
