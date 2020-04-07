import os
import sys

import InstructorProgram as IP
from Config import cfg
from Navigation.structure import Dirs

version = 0.0
dirs = Dirs()


def start():
    print(f'PYG v{version}', end='\n'*2)
    print('Python Grader - Josh Bedwell')
    run()


# main loop-menu function
def run():
    print(f"""{'-'*25}
Options:
[1] Grade/modify an existing assignment
[2] Create a directory for a new assignment
[0] Exit
""")
    choice = IP.input_num_range(0, 2)
    if choice == 1:
        grade()
    if choice == 2:
        make_dir()
    if choice == 0:
        print('\nExiting...')
        sys.exit()


# interact with an assignment
def grade():
    if len(dirs.assignment_dirs) == 0:
        print('\nNo assignment directories have been created')
        run()

    print('Select assignment to grade:')
    dirs.print_dirs()
    print('[0] Cancel\n')
    assignment_num = IP.input_num_range(0, len(dirs.assignment_dirs) + 1) - 1

    if assignment_num == -1:
        run()
    # create a hw object for the selected assignment
    this_hw = dirs.get_hw(assignment_num)

    # check the object that got made to see if it has required directories
    dirs.initialize_dirs(assignment_num)

    # print options for hw object
    print('\nOptions:')
    print('[1] Generate key files')
    print('[2] Export student testing program')
    print('[3] Grade student code')
    print('[4] View grading report')
    print('[0] Cancel\n')
    assignment_option = IP.input_num_range(0, 4)

    if assignment_option == 1:
        this_hw.generate_key_files()

    if assignment_option == 2:
        this_hw.export_student_tester()

    if assignment_option == 3:
        this_hw.grade_student_code()

    if assignment_option == 4:
        this_hw.view_grading_report()

    # if they choose 0 it goes here anyway
    print('Returning to menu...')
    run()


# this is where an assignment directory can be made
def make_dir():
    print('\nCurrent assignments:')
    dirs.print_dirs()
    print('\nCreate a new assignment directory in your base directory (can be changed in config.ini)')
    print('Enter a blank assignment to stop\n')
    while True:
        new_dir = input(f'{cfg.base_directory}{os.sep}')
        if new_dir == '':
            break
        else:
            dirs.create_new(new_dir)
    run()
