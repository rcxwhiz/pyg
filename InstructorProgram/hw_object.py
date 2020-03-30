import os
import shutil
from os.path import join

import Grading
import InstructorProgram as IP
from FileExecution import execute
from Navigation.structure import Dirs


class HWObject:

    def __init__(self, assignment_name):
        # set assignment name and make directory object
        self.assignment_name = assignment_name
        dirs = Dirs()

        # make dir dictionary with all directories relevant to this HW
        self.dir = {'home': join(dirs.base, assignment_name)}
        for other_dir in ['key-output', 'key-source', 'results', 'student-source', 'test-cases',
                          'sag-info.txt']:
            self.dir[other_dir] = join(self.dir['home'], other_dir)

        # make lists for parts and test cases
        self.problem_parts = None
        self.part_weights = {}
        self.test_case_weights = []
        self.total_points = None

    def generate_key_files(self):
        # making sure there are source files and test cases
        if len(os.listdir(self.dir['key-source'])) == 0:
            print(f'No source files found in {self.dir["key-source"]}')
            return None
        if len(os.listdir(self.dir['test-cases'])) == 0:
            print(f'No dirs found in {self.dir["test-cases"]}')
            return None

        # resolve overwriting prveious key output if there is one
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

        # get a list of the finished files using the run key function
        out_file_list = execute.run_key(self.dir['home'])

        # check if there was any illegal code by looking at output files
        for file in out_file_list:
            if ' + ILLEGAL CODE + ' in execute.read_file(file):
                print(execute.read_file(file))
                print('\nGrading criteria cannot be created. Returning to menu...')
                IP.run()

        # find the parts of the assignment from the outfile list
        self.problem_parts = Grading.Text.criteria.find_parts(out_file_list)

        # prompt for total points and points for the parts of the assignments etc...
        self.total_points = IP.tools.input_num_range(1, 100,
                                                     message='\nEnter the total weight of the assignment, 1-100: ')

        if len(self.problem_parts) != 0:
            print(
                f'\n{len(self.problem_parts)} parts detected in the first test case ({os.listdir(self.dir["test-cases"])[0]})')
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

    def export_student_tester(self):
        print('export student tester')

    def grade_student_code(self):
        # in student source there are directories that are full of student code - get that list
        # TODO maybe I could support having zip files here too
        source_dirs = []
        for file in os.listdir(self.dir['student-source']):
            if os.path.isdir(join(self.dir['student-source'], file)):
                source_dirs.append(file)

        # choose which directory of student files they should use
        if len(source_dirs) == 0:
            print(f'No directories with student code found in {self.dir["student-source"]}. Returning to menu...')
            IP.run()
        print('Choose a directory of student files to grade from:')
        for i, source_dir in enumerate(source_dirs):
            print(f'[{i + 1}] - {source_dir}')
        source_dir = join(self.dir['student-source'], source_dirs[IP.tools.input_num_range(1, len(source_dirs)) - 1])

        # get the student ids from teh files in the selected student source directory
        student_ids = set()
        types_found = set()
        for file in os.listdir(source_dir):
            student_ids.add('_'.join(file.split('_')[:3]))
            types_found.add(file.split('.')[-1])
        student_ids = sorted(student_ids)

        # populate a directory that will get filled up and eventually zipped as the report
        grading_dir = join(self.dir['home'], 'TEMP')
        if os.path.exists(grading_dir):
            shutil.rmtree(grading_dir)
        os.mkdir(grading_dir)

        # make a directory for each student in the temp dir
        for student_id in student_ids:
            os.mkdir(join(grading_dir, student_id))

        # make a list of file types to move
        types_to_move = []
        print(f'Submitted file types: {types_found}')
        print('Enter -1 to add all')
        for file_type in types_found:
            choice = IP.tools.input_num_range(0, 1, message=f'Move student {file_type} files\n1 - yes\n0 - no\n')
            if choice == 1:
                types_to_move.append(file_type)
            elif choice == -1:
                types_to_move = list(types_found)
                break

        # move the student source files into the temp folder
        for file in os.listdir(source_dir):
            try:
                if file.split('.')[-1] in types_to_move:
                    file_id = '_'.join(file.split('_')[:3])
                    shutil.copyfile(join(source_dir, file), join(self.dir['home'], 'TEMP', file_id, file))
            except IndexError:
        # TODO I need to have a way to keep track of if I'm adding things without an extension

        # TODO run them all
        # TODO need to have a way to grade the outputs based on if their parts are the same
        # TODO generate a xlsx or something with the student results and scores
        # TODO put everything into a zip file and put that in results and say it's in there
        print('grade student code')

    def view_grading_report(self):
        print('view grading report')
