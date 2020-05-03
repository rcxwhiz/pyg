import configparser
import os
import re
import sys
import typing
from os.path import join

ERASE_LINE = '\x1b[2K'

# TODO need to use this guy to get IDs
id_re = re.compile(r'([^_]*)_([^_]*)_([^_\.]*)')


def get_id(string_in: str) -> typing.Tuple[str, str, str]:
    match = re.match(id_re, string_in)
    if match is None:
        return None
    else:
        return tuple(match[1:])


def erase():
    sys.stdout.write(ERASE_LINE)


def input_range(low: int, high: int, message: str = 'Option: ') -> int:
    answer = -100
    retry = ''
    while answer < low or answer > high:
        try:
            answer = int(input(message + retry))
        except ValueError:
            pass
        retry = f'({low}-{high}) '
    return answer


def generate_blank_rubric(parts: typing.List[str], file_name: str, assignment_name: str) -> None:
    if os.path.exists(file_name):
        os.remove(file_name)

    content = f'# This is the rubric for {assignment_name}\n'
    content += '# Fill in the values so that you can grade this assignment\n\n'

    content += '[Assignment]\n\n# Enter the total weight of the assignment here (ex. 0-100):\n'
    content += 'total_weight=\n\n'

    content += '\n# Enter the relative weights of each problem here (ex. 0-100):\n[Parts]\n\n'
    for part in parts:
        content += f'{(part[0] + part[1]).replace(" ", "_")}=\n'
    content += '\n'

    with open(file_name, 'w') as file:
        file.write(content)


def get_assignment_parts(assignment_dir: str, replace_underscores: bool = True) -> typing.List[str]:
    reader = configparser.ConfigParser()
    reader.read(join(assignment_dir, 'rubric.ini'))
    parts = reader.options('Parts')
    if replace_underscores:
        for i in range(len(parts)):
            parts[i] = parts[i].replace('_', ' ')
    return parts


def get_assignment_test_cases(assignment_dir: str) -> typing.List[str]:
    return os.listdir(join(assignment_dir, 'test-cases'))
