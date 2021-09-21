#!/Users/jeff/.pyenv/shims/python

import re
import sys
import json
import requests

def main():
	try:
		directory = sys.argv[1]
	except:
		raise ValueError('Missing an argument (the directory where the pickled file resides). Exiting...')

	url = 'http://127.0.0.1:5000/rescan'
	response = requests.get(url, params={'directory': f'{directory}'})

	# Clean up the HTML formatting in the response
	result = response.text
	result = re.sub('^.*?<pre>', '', result)
	result = re.sub('</pre>', '', result)
	result = re.sub('<h3>', '   ', result)
	result = re.sub('</h3>', '', result)
	result = re.sub('<br>', '\n', result)
	result = re.sub('&nbsp', '', result)

	try:
		result = json.loads(result)
		result = json.dumps(result, indent = 4)
		print(result)
	except:
		print(result)

if __name__ == '__main__':
	main()



