#!/Users/jeff/.pyenv/shims/python

import string

def create_password_checker(min_uppercase, min_lowercase, \
                            min_punctuation, min_digits):
    """Function to return that checks pw for complexity rules"""
    def checker(pw):
        ### Vars
        rules_dict = {}
        digit_cntr = upper_cntr = lower_cntr = punc_cntr = 0
        special_chars = string.punctuation

        ### Loop through password string checking each char and increment
        ### counters as applicable
        for char in pw:
            if char.isdigit():
                digit_cntr += 1
            elif char.isupper():
                upper_cntr += 1
            elif char.islower():
                lower_cntr += 1
            elif char in special_chars:
                punc_cntr += 1

        ### Append each character class pair to dict
        rules_dict['uppercase'] = (upper_cntr - min_uppercase)
        rules_dict['lowercase'] = (lower_cntr - min_lowercase)
        rules_dict['punctuation'] = (punc_cntr - min_punctuation)
        rules_dict['digits'] = (digit_cntr - min_digits)

        ### If any value in the dict is < 0, set password complexity check to
        ### False and break out of the loop. Otherwise, set check to True and
        ### clobber as necessary.
        for keys,value in rules_dict.items():
            if int(value) < 0:
                tuple = (False, rules_dict)
                break
            elif int(value) >= 0:
                tuple = (True, rules_dict)
        return tuple
    ### Return the checker function to create_password_checker function
    return checker

def  main():
    """Main function for password checker"""

    pc = create_password_checker(2, 3, 1, 4)
    print('\nChecking password for at least: 2 upper chars, 3 lower chars, 1 punctuation char, and 4 digits...\n')
    print('   Password is: AB!1')
    print('   Results tuple is:',pc('Ab!1'))
    print('\n')
    print('   Password is: ABcde!1234')
    print('   Results tuple is:',pc('ABcde!1234'))
    print('\n')

if __name__ == '__main__':
    main()
