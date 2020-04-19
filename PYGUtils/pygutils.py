import os
import sys
import typing

ERASE_LINE = '\x1b[2K'


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


def generate_blank_ruberic(parts: typing.List[str], file_name: str, assignment_name: str) -> None:
    if os.path.exists(file_name):
        os.remove(file_name)

    content = f'# This is the ruberic for {assignment_name}\n'
    content += '# Fill in the values so that you can grade this assignment\n\n'

    content += '[Assignment]\n\n# Enter the total weight of the assignment here (ex. 0-100):\n'
    content += 'total_weight=\n\n'

    content += '[Parts]\n\n# Enter the relative weight of each problem here (ex. 0-100):\n'
    for part in parts:
        content += f'{part}=\n'
    content += '\n'

    with open(file_name, 'w') as file:
        file.write(content)
