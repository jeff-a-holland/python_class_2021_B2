#!/Users/jeff/.pyenv/shims/python

import os
import hashlib
import pickle
from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

def check_dir(directory):
	if os.path.isdir(directory):
		if directory.endswith('/'):
			pass
		else:
			directory += '/'
	return directory

class FileInfo(object):
	"""FileInfo class to create object with list of dictionaries"""
	object_list = []
	file_list = []
	target_dir = ''
	def __init__(self, return_list, directory):
		self.directory = directory
		self.return_list = return_list
		FileInfo.file_list = self.return_list
		FileInfo.target_dir = self.directory

	def get_file_info(self):
		self.filename = ''
		self.timestamp = ''
		self.sha1 = ''

		for file in FileInfo.file_list:
				# Compute timestamp of when file as last changed (in local time)
				self.filename = file
				mtime = os.stat(file).st_mtime
				self.timestamp = datetime.fromtimestamp(mtime) \
					.strftime('%Y-%m-%d-%H:%M')

				# Compute sha1 hash of file, reading in 2^16 bytes at a time in
				# binary mode in case the file is too large for memory
				sha1sum = hashlib.sha1()
				with open(file, 'rb') as source:
					block = source.read(2**16)
					while len(block) != 0:
						sha1sum.update(block)
						block = source.read(2**16)
				self.sha1 = sha1sum.hexdigest()
				FileInfo.object_list.append({'filename': self.filename,
											 'timestamp': self.timestamp,
											 'sha1': self.sha1})
		#print(FileInfo.object_list)
	def scan(self):
		self.pickle_list = []
		self.pickled_obj = b''
		for d in FileInfo.object_list:
			fullfilepath = (d['filename'])
			filedir = os.path.dirname(d['filename'])
			filename = os.path.basename(d['filename'])
			timechanged = (d['timestamp'])
			sha1 = (d['sha1'])
			timeaccessed = datetime.now().strftime('%Y-%m-%d-%H:%M')
			info_dict = {'fullfilepath': fullfilepath, 'filedir': filedir,
						 'filename': filename, 'timechanged': timechanged,
						 'sha1': sha1, 'timeaccessed': timeaccessed}
			self.pickle_list.append(info_dict)

		self.pickled_obj = pickle.dumps(self.pickle_list)
		filelist_fullpath = FileInfo.target_dir + 'FileList'
		if os.path.isfile(filelist_fullpath) == False:
			print('\n################################################################')
			print('Pickled file does not exist. Creating pickle file "FileList" in:')
			print('################################################################')
			print('\n', FileInfo.target_dir)
			with open(filelist_fullpath, 'wb') as fh:
				fh.write(self.pickled_obj)
		else:
			print('\n######################################')
			print('Pickle file "FileList" already exists.')
			print('######################################')
			print('Skipping creation...')

class FileList(FileInfo):
	"""FileList class that subclasses FileInfo to determine if any files were
	changed, removed, or added (based on existence or sha1 hash value). Any files
	that remain unchanged will not be reported upon."""

	def rescan(self):
		filelist_fullpath = self.test_dir + 'FileList'
		with open(filelist_fullpath, 'rb') as fh:
			data = fh.read()
			unpickled_object = pickle.loads(data)
			print('\n#####################################################')
			print('Pickled file "FileList" contents after unpickling is:')
			print('#####################################################\n')
			print(unpickled_object, '\n')

		pickled_files_list = []
		disk_files_list = []
		results_dict = {}
		changed_list = []
		added_list = []
		removed_list = []
		print('###############################################################'
			  '######################')
		print('File changes detected since initial file checksum and pickled '
			  'file baseline creation:')
		print('###############################################################'
			  '######################\n')
		for d in unpickled_object:
			fullfilepath_orig = d['fullfilepath']
			pickled_files_list.append(fullfilepath_orig)
			for file in os.listdir(self.test_dir):
				fullfilepath_new = os.path.join(self.test_dir, file)
				if os.path.isfile(fullfilepath_new) and not fullfilepath_new.endswith('FileList'):
					disk_files_list.append(fullfilepath_new)
					sha1_new = hashlib.sha1(open(fullfilepath_new, 'rb').read()).hexdigest()
					if fullfilepath_orig == fullfilepath_new and \
							d['sha1'] == sha1_new:
						print(f'exiting file "{fullfilepath_orig}" unchanged')
					elif fullfilepath_orig == fullfilepath_new and \
							d['sha1'] != sha1_new:
						changed_list.append(fullfilepath_orig)
						print(f'existing file "{fullfilepath_orig}" CHANGED')

		for file in pickled_files_list:
			if file not in disk_files_list:
				removed_list.append(file)
				print(f'previous file "{file}" was REMOVED')
				break
		for file in disk_files_list:
			if file not in pickled_files_list:
				added_list.append(file)
				print(f'new file "{file}" was ADDED')
				break
		results_dict = {'added': added_list, 'removed': removed_list, 'changed': changed_list}
		print('\n######################################')
		print('results_dict with all file changes is:')
		print('######################################\n')
		print(results_dict, '\n')
		return results_dict

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

		fi = FileInfo(results_list, directory)
		fi.get_file_info()
		fi.scan()
		result = '<h3>Pickling the following files and creating file hash database'\
				 ' on disk:</h3>' + '<br>'.join(results_list)

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
