import os
import shutil
from os.path import join

import Grading
import InstructorProgram as IP
from FileExecution import execute
from Navigation.structure import Dirs


class HWObject:
    def __init__(self, assignment_num):
        self.assignment_num = assignment_num
        self.dirs = Dirs()

        self.dir = {'home': join(self.dirs.base, self.dirs.assignment_dirs[assignment_num])}
        for other_dir in ['custom criteria', 'key-output', 'key-source', 'results', 'student-source', 'test-cases',
                          'sag-info.txt']:
            self.dir[other_dir] = join(self.dir['home'], other_dir)
        self.problem_parts = None
        self.test_cases = os.listdir(self.dir['test-cases'])

        self.part_weights = {}
        self.test_case_weights = []
        self.total_points = None

    def check_full(self):
        return self.dirs.check_full(self.assignment_num)

    def generate_key_files(self):
        if len(os.listdir(self.dir['key-output'])) > 0:
            print('[1] Overwrite current key files')
            print('[0] Don\'t overwrite current key files')
            choice = IP.tools.input_num_range(0, 1)
            if choice == 1:
                k = 0
                while True:
                    k += 1
                    if k > 25:
                        print(f'There was an issue clearing {self.dir["key output"]}')
                        IP.run()
                    try:
                        shutil.rmtree(self.dir['key-output'], ignore_errors=True)
                        os.mkdir(self.dir['key-output'])
                        break
                    except FileExistsError:
                        continue
                    except PermissionError:
                        print(f'Permission error clearing the directory {self.dir["key-output"]}'
                              f'Please close it if it is open')
                        IP.run()
            else:
                return None

        out_file_list = execute.run_key(self.dir['home'])
        self.problem_parts = Grading.Text.criteria.find_parts(out_file_list)

        print('\nEnter the total weight of the assignment, 1-100:')
        self.total_points = IP.tools.input_num_range(1, 100)

        print(f'\n{len(self.problem_parts)} parts detected in {len(self.test_cases)} test cases')
        print('Parts:', end=' ')
        print_parts = []
        for part in self.problem_parts:
            print_parts.append(f'{part[0]} {part[1]}')
        print(', '.join(print_parts))
        print('Enter the point weight of each part 0-100, -1 to weight all evenly:')
        for part in self.problem_parts:
            part_weight = IP.tools.input_num_range(-1, 100, message=f'{part[0]} {part[1]}: ')
            if part_weight == -1:
                for part2 in self.problem_parts:
                    self.part_weights[part2[1]] = 10
                break
            self.part_weights[part[1]] = part_weight

        # TODO now make a way to enter the weights of different test cases

    def export_student_tester(self):
        print('export student tester')

    def grade_student_code(self):
        print('grade student code')

    def view_grading_report(self):
        print('view grading report')
