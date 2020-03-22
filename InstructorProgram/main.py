import sys

import InstructorProgram as IP
from Config import cfg
from Navigation.structure import Dirs

version = 0.0
dirs = Dirs()


def run(display_title=True):
    if display_title:
        print(f"""
The Squad Automatic Grader
-----------------------------------------

Version - {version}

Options:
[1] Grade from an existing directory
[2] Create a directory for a new HW
[0] Exit
""")
    choice = IP.tools.input_num_range(0, 2)
    if choice == 1:
        grade()
    if choice == 2:
        make_dir()
    if choice == 0:
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
