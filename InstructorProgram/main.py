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
    print('[0] Cancel\n')
    assignment_num = IP.tools.input_num_range(0, len(dirs.assignment_dirs) + 1) - 1

    if assignment_num == -1:
        run()
    this_hw = IP.HWObject(assignment_num)

    errors = this_hw.check_full()
    if len(errors) > 0:
        print('\n'.join(errors))
        print('Returning to menu...')
        run()

    print('\nOptions:')
    print('[1] Generate key files')
    print('[2] Export student testing program')
    print('[3] Grade student code')
    print('[4] View grading report')
    print('[0] Cancel\n')
    assignment_option = IP.tools.input_num_range(0, 4)

    if assignment_option == 1:
        try:
            this_hw.generate_key_files()
        except RuntimeError:
            print('Returning to menu...')
            run()

    if assignment_option == 2:
        print('')
    if assignment_option == 3:
        print('')
    if assignment_option == 4:
        print('')
    if assignment_option == 0:
        run()

    # enter a menu with the following options
    # [1] generate key files
    # There needs to be some option to only have 1 test case I guess for problems where data will not be loaded
    # [2] export student's grading program
    # [3] run student code
    # [4] visually look at the code student's submitted (like my old program)
    # When running code on threads it might be the best idea to just clear the screen with a bunch of new lines?

    run()


def make_dir():
    print('\nCurrent directories:')
    dirs.print_dirs()
    print('\nCreate a new assignment directory in your base directory (can be changed in config.ini)')
    print('Enter a blank directory to stop\n')
    while True:
        new_dir = input(f'{cfg.base_directory}/')
        if new_dir == '':
            break
        else:
            dirs.create_new(new_dir)
    run()
