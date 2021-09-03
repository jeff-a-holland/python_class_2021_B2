#!/Users/jeff/.pyenv/shims/python

import os
import hashlib
import pickle
from datetime import datetime

class FileInfo(object):
    """FileInfo class to create object with list of dictionaries"""
    object_list = []
    def __init__(self, test_dir):
        self.test_dir = test_dir

    def get_file_info(self):
        self.filename = ''
        self.timestamp = ''
        self.sha1 = ''

        for file in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, file)

            if os.path.isfile(file_path) and not file_path.endswith('FileList'):
                # Compute timestamp of when file as last changed (in local time)
                self.filename = file_path
                mtime = os.stat(file_path).st_mtime
                self.timestamp = datetime.fromtimestamp(mtime) \
                    .strftime('%Y-%m-%d-%H:%M')

                # Compute sha1 hash of file, reading in 2^16 bytes at a time in
                # binary mode in case the file is too large for memory
                sha1sum = hashlib.sha1()
                with open(file_path, 'rb') as source:
                    block = source.read(2**16)
                    while len(block) != 0:
                        sha1sum.update(block)
                        block = source.read(2**16)
                self.sha1 = sha1sum.hexdigest()
                FileInfo.object_list.append({'filename': self.filename,
                                             'timestamp': self.timestamp,
                                             'sha1': self.sha1})

class FileList(FileInfo):
    """FileList class that subclasses FileInfo to determine if any files were
    changed, removed, or added (based on existence or sha1 hash value). Any files
    that remain unchanged will not be reported upon."""
    pickle_list = []
    pickled_obj = b''
    def scan(self):  # sourcery skip: extract-duplicate-method
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
            FileList.pickle_list.append(info_dict)

        FileList.pickled_obj = pickle.dumps(FileList.pickle_list)
        filelist_fullpath = self.test_dir + 'FileList'
        if os.path.isfile(filelist_fullpath) == False:
            print('\n################################################################')
            print('Pickled file does not exist. Creating pickle file "FileList" in:')
            print('################################################################')
            print('\n', self.test_dir)
            with open(filelist_fullpath, 'wb') as fh:
                fh.write(FileList.pickled_obj)
        else:
            print('\n######################################')
            print('Pickle file "FileList" already exists.')
            print('######################################')
            print('Skipping creation...')

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

def main():
    # Testing directory. Modify as necessary.
    test_dir = '/Users/jeff/Documents/GitHub/python_class_2021_B2/exercise_11/'

    fi = FileInfo(test_dir)
    fi.get_file_info()

    fl = FileList(test_dir)
    fl.scan()
    fl.rescan()

if __name__ == '__main__':
    main()