import Config as cfg
from PYGUtils import *

VERSION = '0.0'
navi = Navigator()


def main() -> None:
    # TODO this is an example and should be removed
    os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
    print(os.getcwd())

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

        choice = input_range(0, 3)

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

    if len(navi.assignment_dirs) == 0:
        print('No assignment directories have been created')
        return None

    print('Select an assignment to grade:')
    navi.print_dirs()
    print('[0] Cancel\n')
    assignment_num = input_range(0, len(navi.assignment_dirs) + 1) - 1

    if assignment_num == -1:
        return None

    assignment = navi.get_assignment(assignment_num)

    print('\nOptions:')
    print('[1] Generate key files')
    print('[2] Export student testing program')
    print('[3] Automatically grade student code')
    print('[4] Manually grade student code')
    print('[4] View grading report')
    print('[0] Cancel\n')
    assignment_option = input_range(0, 4)

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
    print('\nCurrent assignments:')
    navi.print_dirs()
    print(f'\nAssignment will be created in {cfg.base_directory}{os.sep}')
    print('Enter a blank name to cancel')

    new_dir = input('New assignment name: ')

    if new_dir in os.listdir(cfg.base_directory):
        print('There is already an assignment with that name')
    elif new_dir != '':
        navi.create_new(new_dir)


if __name__ == '__main__':
    main()
