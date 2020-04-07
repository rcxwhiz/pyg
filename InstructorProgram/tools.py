import os


# this function just makes sure you get a value in the range
def input_num_range(low, high, message='Option: '):
    answer = -100
    while answer < low or answer > high:
        try:
            answer = int(input(message))
        except ValueError:
            continue
    return answer


def generate_blank_ruberic(parts, file_name, assignment_name):
    if os.path.exists(file_name):
        os.remove(file_name)

    content = f'# This is the ruberic for {assignment_name}\n'
    content += '# Fill in the values so that you can grade this assignment\n\n'

    content += '# Enter the total weight of the assignment here (ex. 0-100):\n'
    content += 'total_weight=\n\n'

    content += '# Enter the relative weight of each problem here (ex. 0-100):\n'
    for part in parts:
        content += f'{part}=\n'
    content += '\n'

    with open(file_name, 'w') as file:
        file.write(content)
