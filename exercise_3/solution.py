#!/Users/jeff/.pyenv/shims/python

import os
import glob
import queue
from threading import Thread

def count_words_sequential(arg):
    """Function for counting words in files sequentially"""
    words = 0
    for file in glob.glob(arg):
        if os.path.isfile(file) == True:
            with open(file, 'r') as fh:
                for line in fh:
                    line = line.rstrip('\n')
                    words_list = line.split()
                    words += len(words_list)
    print('\n###############################################################')
    print(f'Sequential Solution:\n     Number of words in all files is: {words}')
    print('###############################################################\n')
    return words


def count_words_threading(arg):
    """Function for counting words in files using threading and a queue"""

    def count_words(q, filename):
        """Inner function called in thread worker object to count words in file"""
        file = q.get()
        if os.path.isfile(file) == True:
            with open(file, 'r') as fh:
                print(f'      Counting lines in file "{file}" from Queue object: {q}')
                for line in fh:
                    line = line.rstrip('\n')
                    words_list = line.split()
                    # Add count of each line in each file to a list. We'll sum
                    # them later.
                    words_threaded_list.append(len(words_list))
        q.task_done()

    # Global vars in count_words_threading function.
    words = 0
    words_threaded_list = []
    file_list = []

    # Build file_list with names of files to count words in.
    for file in glob.glob(arg):
        if os.path.isfile(file) == True:
            file_list.append(file)

    # Instantiate q object and set number of threads based on length of
    # file_list.
    q = queue.Queue(maxsize=0)
    num_threads = len(file_list)

    print('\n###############################################################')
    print('Threading Solution:')
    print('      Files are:\n      ------------------------------------------------')
    for value in file_list:
        print(f'      {file}')
    print('      ------------------------------------------------')
    print(f'\n      Number of threads is: {num_threads}\n')

    # Put files into the q object.
    for file in file_list:
        q.put(file)

    # Create worker threads.
    for num in range(num_threads):
        filename = file_list[num]
        worker = Thread(target=count_words, args=(q, filename,))
        print(f'      Thread {num} worker is: {worker}\n')
        worker.setDaemon(True)
        worker.start()

    # Block until all tasks are done.
    q.join()

    # Determine total number of words in all files after thread processing
    # has finished.
    for int in words_threaded_list:
        words += int
    print(f'\n      Number of words in all files is: {words}')
    print('###############################################################\n')
    return(words)

def main():

    ### TESTING START
    dir = '/Users/jeff/Documents/GitHub/python_class_2021_B2/exercise_3/'
    files = '*.txt'
    arg = dir + files
    count_words_sequential(arg)
    count_words_threading(arg)
    ### TESTING END

if __name__ == '__main__':
    main()
