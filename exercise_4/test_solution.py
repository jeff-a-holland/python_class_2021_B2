#!/Users/jeff/.pyenv/shims/python
from solution import create_password_checker
from string import ascii_uppercase as uppercase, ascii_lowercase as lowercase, punctuation, digits
import pytest

def test_no_min_no_pw():
    pc = create_password_checker(0,0,0,0)
    result, details = pc('')

    assert result
    for key, value in details.items():
        assert value == 0

def test_no_min_some_pw():
    pc = create_password_checker(0,0,0,0)
    result, details = pc('ABCDefgh!@#$1234')

    assert result
    for key, value in details.items():
        assert value == 4

def test_simple_good():
    pc = create_password_checker(1,2,3,4)
    result, details = pc('Abc!@#1234')
    assert result
    for key, value in details.items():
        assert value == 0

def test_simple_bad():
    pc = create_password_checker(1,2,3,4)
    result, details = pc('b!#234')
    assert result == False
    for key, value in details.items():
        assert value == -1

@pytest.mark.parametrize('onlyset', [
    'uppercase',
    'lowercase',
    'punctuation',
    'digits'])
def test_only_set_one(onlyset):
    for source in ['uppercase', 'lowercase', 'punctuation', 'digits']:
        if onlyset == source:
            pw = globals()[source][:4]

    pc = create_password_checker(4,4,4,4)
    result, details = pc(pw)

    assert result == False
    for key, value in details.items():
        if key == onlyset:
            assert value == 0
        else:
            assert value == -4

@pytest.mark.parametrize('donotset', [
    'uppercase',
    'lowercase',
    'punctuation',
    'digits'])
def test_only_ignore_one(donotset):
    pw = ''
    for source in ['uppercase', 'lowercase', 'punctuation', 'digits']:
        if donotset == source:
            continue
        pw += globals()[source][:4]

    pc = create_password_checker(4,4,4,4)
    result, details = pc(pw)

    assert result == False
    for key, value in details.items():
        if key == donotset:
            assert value == -4
        else:
            assert value == 0
