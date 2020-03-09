import sys

import InstructorProgram as IP
from Config import cfg
from Navigation.structure import Dirs

dirs = Dirs()


def run(display_title=True):
    if display_title:
        print(IP.title.title_string)
    choice = IP.tools.input_num_range(1, 3)
    if choice == 1:
        grade()
    if choice == 2:
        make_dir()
    if choice == 3:
        print('\nExiting...')
        sys.exit()


def grade():
    if len(dirs.assignment_dirs) == 0:
        print('\nNo assignment directories created.')
        run()
    print('Select assignment to grade:')
    dirs.print_dirs()
    print('')
    assignment_num = IP.tools.input_num_range(1, len(dirs.assignment_dirs)) - 1

    errors = dirs.check_full(assignment_num)
    if len(errors) > 0:
        print('\n'.join(errors))
        run()

    # if it got here it is time to grade I guess

    run()


def make_dir():
    print('\nCurrent directories:')
    dirs.print_dirs()
    print('\nCreate a new assignment directory in your base directory (can be changed in config.ini)')
    print('Enter a blank directory to stop\n')
    while True:
        new_dir = input(f'{cfg.base_directory}\\')
        if new_dir == '':
            break
        else:
            dirs.create_new(new_dir)
    run()
