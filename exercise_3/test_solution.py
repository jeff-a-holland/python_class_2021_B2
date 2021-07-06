#!/Users/jeff/.pyenv/shims/python

from solution import count_words_sequential, count_words_threading

def test_non_threaded_empty_dir(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    assert 0 == count_words_sequential(str(test_directory / '*.txt'))


def test_non_threaded_dirname(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    test_subdir = test_directory / 'subdir'
    test_subdir.mkdir()

    assert 0 == count_words_sequential(str(test_directory / '*d*'))


def test_non_threaded_one_empty_file(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    with open(test_directory / f'mytestfile.txt', 'w') as f:
        f.write('')

    assert 0 == count_words_sequential(str(test_directory / '*.txt'))


def test_non_threaded_five(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    s = 'abc def ghi jkl mno'
    for filename in ['abc', 'def', 'ghi']:
        with open(test_directory / f'{filename}.txt', 'w') as f:
            f.write(s)

    assert 15 == count_words_sequential(str(test_directory / '*.txt'))


def test_threaded_empty_dir(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    assert 0 == count_words_threading(str(test_directory / '*.txt'))


def test_threaded_dirname(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    test_subdir = test_directory / 'subdir'
    test_subdir.mkdir()

    assert 0 == count_words_threading(str(test_directory / '*d*'))


def test_threaded_one_empty_file(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    with open(test_directory / f'mytestfile.txt', 'w') as f:
        f.write('')

    assert 0 == count_words_threading(str(test_directory / '*.txt'))


def test_threaded_five(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    s = 'abc def ghi jkl mno'
    for filename in ['abc', 'def', 'ghi']:
        with open(test_directory / f'{filename}.txt', 'w') as f:
            f.write(s)

    assert 15 == count_words_threading(str(test_directory / '*.txt'))
