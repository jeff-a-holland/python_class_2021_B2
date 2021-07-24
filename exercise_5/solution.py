#!/Users/jeff/.pyenv/shims/python

import argparse
import textwrap

def main():
    """Main function for headtail program"""

    ###Configure command line options using argparse
    parser = argparse.ArgumentParser(formatter_class=\
                                     argparse.RawTextHelpFormatter)
    parser.add_argument('--start', '-s', nargs='?', const=1, type=int, default=3)
    parser.add_argument('--end', '-e', nargs='?', const=1, type=int, default=3)
    parser.add_argument('filename', nargs='+', help=textwrap.dedent('''
NOTES:
- Enter the positional required argument "filename". You can enter the name
  of an existing file in the current directory, or "tmpfile" which is
  auto-generated with a default of 100 lines.
- Enter the optional argument for the number of lines to print from the
  beginning (head) of the file (-s <int> or --start <int>).
- Enter the optional argument for the number of lines to print from the
  end (tail) of the file (-e <int> or --end <int>).

- For example: ./solution.py tmpfile -s 2 -e 2
               OR
               ./solution.py tmpfile

- If no value is given for --start and/or --end, a default of 3 will be used.

- Use -h or --help for help info as noted above.'''))

    args = parser.parse_args()

    ### Create a file to parse head and tail lines from
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

    ### Determine lines in existing local file supplied as an arg instead of
    ### the auto-generated "tmpfile"
    if args.filename[0] != 'tmpfile':
        with open(args.filename[0], 'r') as fh:
            file_list = fh.readlines()
            num_lines = len(file_list)

    ### Determine number of lines requested from start and end arguments and
    ### print them from the <filename> if there are enough lines. Otherwise,
    ### error out.
    if args.start + args.end <= num_lines:
        print(f'\nPrinting {args.start} line(s) from head and {args.end} line(s)'
              f' from tail of the "{args.filename[0]}" file.\nUsing the -s and '
              '-e arguments value, or the default value "3" if either was not '
              'given...\n')

        with open(args.filename[0], 'r') as fh:
            file_list = fh.readlines()

        for index,value in enumerate(file_list):
            value = value.replace('\n', '')
            file_list[index] = value

        head_list = file_list[:args.start]
        tail_list =  file_list[-args.end:]
        for value in head_list:
            print(value)
        print('...')
        for value in tail_list:
            print(value)
        print('\n')

    else:
        raise ValueError(f'\n\nCannot print {args.start + args.end} lines from a file with {num_lines} lines.\n\nExiting!!\n')

if __name__ == '__main__':
    main()
