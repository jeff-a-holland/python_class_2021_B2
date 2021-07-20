#!/Users/jeff/.pyenv/shims/python

import argparse
import textwrap

def main():
    """Main function for headtail program"""

    ###Configure command line options using argparse
    parser = argparse.ArgumentParser(formatter_class=\
                                     argparse.RawTextHelpFormatter)
    parser.add_argument('--lines', '-l', nargs='?', const=1, type=int, default=3,
                        help=textwrap.dedent('''
NOTES:
- Enter the number of lines that you want to print from the beginning (head)
  and from the end (tail) of the auto-generated file using "-l <number>" or
  "--lines <number>".

- For example: ./solution.py --lines 4
               OR
               ./solution.py -l 4

- If no value is given for LINES, a default of 3 will be used.

- Use -h or --help for help info as noted above.

  '''))
    args = parser.parse_args()

    ### Create a file to run parse head and tail lines from
    num_lines = 100
    cntr = 1
    print(f'\nCreating a file with {num_lines} lines called "tmpfile" in the '
          'local directory...')
    with open('./tmpfile', 'w+') as fh:
        while cntr <= num_lines:
            if cntr == 100:
                fh.write(f'line_{cntr}')
            else:
                fh.write(f'line_{cntr}\n')
            cntr += 1

    ### Determine number of lines requested from LINES argument and print them
    ### from the tmpfile if there are enough lines. Otherwise, error out.
    if args.lines * 2 <= num_lines:
        print(f'\nPrinting {args.lines} lines from head and tail of '
              'the auto-generated file "tmpfile".\nUsing the LINES argument '
              'value, or the default value "3" if one was not given...\n')
        with open('./tmpfile', 'r') as fh:
            file = fh.read()
            file_list = file.split('\n')
        head_list = file_list[:args.lines]
        tail_list =  file_list[-args.lines:]
        for value in head_list:
            print(value)
        print('...')
        for value in tail_list:
            print(value)
        print('\n')

    else:
        raise ValueError(f'\n\nCannot print {args.lines*2} lines from a file '
                         f'with {num_lines} lines.\n\nExiting!!\n')

if __name__ == '__main__':
    main()
