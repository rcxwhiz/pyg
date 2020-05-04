import os
from os.path import join

import Assignment.static_assignment as assignment
import Config as cfg
import GUIFileSelector as gfs
import PYGUtils as putil

VERSION = '0.0'


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
        print('[2] Create a directory for a new assignment')
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
    print('\nChoose an assignment directory')
    assignment_dir = gfs.get_directory(title='Open Assignment Directory')
    if assignment_dir == '':
        return None

    print('\nOptions:')
    print('[1] Generate key files')
    print('[2] Export student testing program')
    print('[3] Automatically grade student code')
    print('[4] Manually grade student code')
    print('[5] View grading report')
    print('[0] Cancel\n')
    assignment_option = putil.input_range(0, 5)

    if assignment_option == 1:
        assignment.generate_key_files(assignment_dir)

    if assignment_option == 2:
        assignment.export_tester(assignment_dir)

    if assignment_option == 3:
        assignment.auto_grade(assignment_dir)

    if assignment_option == 4:
        assignment.manual_grade(assignment_dir)

    if assignment_option == 5:
        assignment.view_grade_report(assignment_dir)

    print('Returning to menu...')


def make_dir() -> None:
    print('\nCreate and select a new assignment directory...')
    assignment_dir = gfs.get_directory(title='Select New Assignment Directory')
    if assignment_dir == '':
        return None
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
    print(f'Made assignment dir {assignment_dir}')


if __name__ == '__main__':
    main()
