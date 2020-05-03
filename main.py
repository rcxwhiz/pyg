import os
from os.path import join

import Config as cfg
import GUIFileSelector as gfs
import PYGUtils as putil

VERSION = '0.0'


# navi = Navigator()


def main() -> None:
    if cfg.show_warning:
        print(open('warning.txt', 'r', encoding='utf-8').read())
        input('Press enter to continue...')
        print('\n')

    print(f'PYG v{VERSION}')
    print('Python Grader - Josh Bedwell')

    while True:
        print('\nMenu')
        print('-' * 25)
        print('Options:')
        print('[1] Grade/modify an existing assignment')
        # print('[2] Create a directory for a new assignment')
        print('[3] About')
        print('[0] Exit')

        choice = putil.input_range(0, 3)

        if choice == 1:
            grade()
        if choice == 2:
            make_dir()
        if choice == 3:
            print(open('info.txt', 'r', encoding='utf=8').read())
        if choice == 0:
            return None


def grade() -> None:
    print('')

    # if len(navi.assignment_dirs) == 0:
    #     print('No assignment directories have been created')
    #     return None
    #
    # print('Select an assignment to grade:')
    # navi.print_dirs()
    # print('[0] Cancel\n')
    # assignment_num = input_range(0, len(navi.assignment_dirs) + 1) - 1
    #
    # if assignment_num == -1:
    #     return None
    #
    # assignment = navi.get_assignment(assignment_num)

    assignment_dir = gfs.get_directory(title='Open Assignment Directory')
    print(assignment_dir)

    print('\nOptions:')
    print('[1] Generate key files')
    print('[2] Export student testing program')
    print('[3] Automatically grade student code')
    print('[4] Manually grade student code')
    print('[4] View grading report')
    print('[0] Cancel\n')
    assignment_option = putil.input_range(0, 4)

    # TODO change all these assignment things to static functions
    if assignment_option == 1:
        assignment.generate_key_files()

    if assignment_option == 2:
        assignment.export_student_tester()

    if assignment_option == 3:
        assignment.auto_grade_student_code()

    if assignment_option == 4:
        assignment.manual_grade_student_code()

    if assignment_option == 5:
        assignment.view_grading_report()

    print('Returning to menu...')


def make_dir() -> None:
    assignment_dir = gfs.get_directory(title='Select New Assignment Directory')
    if len(os.listdir(assignment_dir)) > 0:
        print(f'There are files in {assignment_dir}, do you still want to make an assignment here?')
        print(f'Files will not be overriden')
        print(f'[1] Make assignment in {assignment_dir}')
        print(f'[2] Choose another location')
        print(f'[0] Return to menu')
        choice = putil.input_range(0, 2)

        if choice == 2:
            make_dir()
            return None
        if choice == 0:
            return None

    for required_dir in putil.required_assignment_dirs:
        if not os.path.exists(join(assignment_dir, required_dir)):
            os.mkdir(join(assignment_dir, required_dir))


if __name__ == '__main__':
    main()
