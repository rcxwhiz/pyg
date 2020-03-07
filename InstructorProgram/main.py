import sys

import InstructorProgram as IP


def run(display_title=True):
    if display_title:
        print(IP.title.title_string)
    choice = IP.tools.input_num_range([1, 3])
    if choice == 1:
        grade()
    if choice == 2:
        make_dir()
    if choice == 3:
        sys.exit()


def grade():
    print('grading')
    run()


def make_dir():
    print('making dir')
    run()
