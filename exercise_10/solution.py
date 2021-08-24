#!/Users/jeff/.pyenv/shims/python

import os
import datetime
import hashlib

def get_file_info(pathname):
    """Function to return a list of dicts that contain file path/name, timestamp
    in local time when file was last updated, and sha1 hash of the file"""

    results_list = []
    for file in os.listdir(pathname):
        file_path = os.path.join(pathname, file)

        if os.path.isfile(file_path):
            ## Compute timestamp of when file as last changed (in local time)
            mtime = os.stat(file_path).st_mtime
            timestamp_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d-%H:%M')

            ## Compute sha1 hash of file, reading in 2^16 bytes at a time in
            ## binary mode in case the file is too large for memory
            sha1sum = hashlib.sha1()
            with open(file_path, 'rb') as source:
                block = source.read(2**16)
                while len(block) != 0:
                    sha1sum.update(block)
                    block = source.read(2**16)

            results_list.append({'filename': file_path, \
                                 'timestamp': timestamp_str, \
                                 'sha1': sha1sum.hexdigest()})

    print(f'\nList of dicts containg filename, timestamp, and sha1 hash is:\n\n{results_list}\n')
    return results_list

def main():
    """Main function for get_file_info function"""

    ## Test on current workind directory
    get_file_info('.')

if __name__ == '__main__':
    main()
