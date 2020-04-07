import os
import shutil
from datetime import datetime
from os.path import join
from zipfile import ZipFile

import Grading
import InstructorProgram as IP
from FileExecution import execution
from Navigation.structure import Dirs

no_ext_msg = 'no-extension'


class Assignment:

    def __init__(self, assignment_name):
        # TODO this should not need to be pickled anymore
        # set assignment name and make directory object
        self.assignment_name = assignment_name
        dirs = Dirs()

        # make dir dictionary with all directories relevant to this HW
        self.dir = {'home': join(dirs.base, assignment_name)}
        for other_dir in ['key-output', 'key-source', 'results', 'student-source', 'test-cases',
                          'TEMP']:
            self.dir[other_dir] = join(self.dir['home'], other_dir)

        # self.criteria = None

    def can_run_key(self):
        if len(os.listdir(self.dir['key-source'])) == 0:
            print(f'No source files found in {self.dir["key-source"]}')
            return False
        if len(os.listdir(self.dir['test-cases'])) == 0:
            print(f'No dirs found in {self.dir["test-cases"]}')
            return False
        return True

    def clear_key(self):
        print('[1] Overwrite current key files')
        print('[0] Don\'t overwrite current key files')
        choice = IP.input_num_range(0, 1)
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
            return True
        else:
            return False

    # def set_criteria(self, problem_parts):
    #     # prompt for total points and points for the parts of the assignments etc...
    #     total_points = IP.input_num_range(1, 100, message='\nEnter the total weight of the assignment, 1-100: ')
    #
    #     part_weights = {}
    #     prog_points = False
    #     if len(problem_parts) != 0:
    #         print(
    #             f'\n{len(problem_parts)} parts detected in the first test case ({os.listdir(self.dir["test-cases"])[0]})')
    #         print('Parts:', end=' ')
    #         print_parts = []
    #         for part in problem_parts:
    #             print_parts.append(f'{part[0]} {part[1]}')
    #         print(', '.join(print_parts))
    #         print('Enter the point weight of each part 0-100, -1 to weight all evenly:')
    #         for part in problem_parts:
    #             part_weight = IP.input_num_range(-1, 100, message=f'{part[0]} {part[1]}: ')
    #             if part_weight == -1:
    #                 for part2 in problem_parts:
    #                     part_weights[part2[1]] = 10
    #                 break
    #             part_weights[part[1]] = part_weight
    #
    #         print('Progressive points? (part 2 cannot be passed without part 1)')
    #         print('[1] - yes')
    #         print('[0] - no')
    #         if IP.input_num_range(0, 1) == 1:
    #             prog_points = True
    #
    #     self.criteria = Grading.Text.text.Criteria(part_weights, total_points, self.dir['key-output'], prog_points)

    def generate_key_files(self):
        # making sure there are source files and test cases
        if not self.can_run_key():
            return None

        # resolve overwriting prveious key output if there is one
        if len(os.listdir(self.dir['key-output'])) > 0:
            if not self.clear_key():
                return None

        # get a list of the finished files using the run key function
        out_file_list = execution.run_key(self.dir['home'])

        # check if there was any illegal code by looking at output files
        for file in out_file_list:
            if ' + ILLEGAL CODE + ' in execution.read_file(file):
                print(execution.read_file(file))
                print('\nGrading criteria cannot be created. Returning to menu...')
                IP.run()

        # find the parts of the assignment from the outfile list
        problem_parts = Grading.Text.text.find_parts(out_file_list)

        IP.tools.generate_blank_ruberic(problem_parts, join(self.dir['home'], 'ruberic.ini'), self.assignment_name)
        print(f'Please fill out {join(self.dir["home"], "ruberic.ini")}')
        print('in order to be able to grade the file.')

    def export_student_tester(self):
        print('export student tester')

    def choose_student_source_dir(self):
        # TODO maybe I could support having zip files here too for holding student code
        source_dirs = []
        for file in os.listdir(self.dir['student-source']):
            if os.path.isdir(join(self.dir['student-source'], file)):
                source_dirs.append(file)

        # choose which directory of student files they should use
        if len(source_dirs) == 0:
            print(f'No directories with student code found in {self.dir["student-source"]}. Returning to menu...')
            IP.run()
        print('Choose a batch of student files to grade from:')
        for i, source_dir in enumerate(source_dirs):
            print(f'[{i + 1}] - {source_dir}')
        return join(self.dir['student-source'], source_dirs[IP.input_num_range(1, len(source_dirs)) - 1])

    def get_ids_from_files(self, source_dir):
        student_ids = set()
        types_found = set()
        for file in os.listdir(source_dir):
            if '.' not in file:
                types_found.add(no_ext_msg)
            else:
                student_ids.add('_'.join(file.split('_')[:3]))
                types_found.add(file.split('.')[-1])
        return sorted(student_ids), types_found

    def make_temp_dir(self, student_ids):
        # populate a directory that will get filled up and eventually zipped as the report
        if os.path.exists(self.dir['TEMP']):
            shutil.rmtree(self.dir['TEMP'])
        os.mkdir(self.dir['TEMP'])

        # make a directory for each student in the temp dir
        for student_id in student_ids:
            os.mkdir(join(self.dir['TEMP'], student_id))

    def get_types_to_move(self, types_found):
        types_to_move = []
        print(f'\nSubmitted file types: {types_found}')
        print('Enter 2 to add all')
        for file_type in types_found:
            choice = IP.input_num_range(0, 2, message=f'Move student .{file_type} files\n[1] - yes\n[0] - no\n')
            if choice == 1:
                types_to_move.append(file_type)
            elif choice == 2:
                types_to_move = list(types_found)
                break
        return types_to_move

    def move_student_files(self, source_dir, types_to_move):
        # I HAVE DECIDED TO REMOVE THE IDS FROM THE FILES HERE
        for file in os.listdir(source_dir):
            try:
                if file.split('.')[-1] in types_to_move:
                    file_id = '_'.join(file.split('_')[:3])
                    file_name = '_'.join(file.split('_')[3:])
                    shutil.copyfile(join(source_dir, file), join(self.dir['TEMP'], file_id, file_name))
            except IndexError:
                if no_ext_msg in types_to_move:
                    file_id = '_'.join(file.split('_')[:3])
                    file_name = '_'.join(file.split('_')[3:])
                    shutil.copyfile(join(source_dir, file), join(self.dir['TEMP'], file_id, file_name))

    def zip_report(self):
        # Note this will only go one folder deep into the temp folder, but this shouldn't be an issue
        timestamp = datetime.now().strftime('%d-%b-%Y %I-%M-%S %p')
        with ZipFile(f'{join(self.dir["results"], timestamp)}.zip', 'w') as zip_obj:
            for folder in os.listdir(self.dir['TEMP']):
                if os.path.isdir(join(self.dir['TEMP'], folder)):
                    for file in os.listdir(join(self.dir['TEMP'], folder)):
                        zip_obj.write(join(self.dir['TEMP'], folder, file), arcname=join(folder, file))
                else:
                    zip_obj.write(join(self.dir['TEMP'], file), arcname=file)
        shutil.rmtree(self.dir['TEMP'])

    def grade_student_code(self):
        # TODO need to load the ini file (make a function in tools) and catch any errors loading it

        source_dir = self.choose_student_source_dir()

        # get the student ids from the files in the selected student source directory
        student_ids, types_found = self.get_ids_from_files(source_dir)

        self.make_temp_dir(student_ids)

        # make a list of file types to move
        types_to_move = self.get_types_to_move(types_found)

        # move the student source files into the temp folder
        self.move_student_files(source_dir, types_to_move)

        # run the student code on a bunch of threads and leaves the output.txt s
        out_files = execution.run_students(self.dir['TEMP'])
        # TODO need to have a way to grade the outputs based on if their parts are the same
        # TODO generate a xlsx or something with the student results and scores

        # make a zip file in results and copy everything from temp into it
        self.zip_report()

    def view_grading_report(self):
        # TODO make reporter object and pass it to the UI
        # TODO this should also pop up a seperate window with the xlsx report (this would have to be from the program)

        if len(os.listdir(self.dir['results'])) == 0:
            print(f'No reports have been generated for {self.assignment_name} yet.')
            return None

        zips = []
        for file in os.listdir(self.dir['results']):
            if file.endswith('.zip'):
                zips.append(file)
        print('Choose report to view:')
        for i, file in enumerate(zips):
            print(f'[{i}] {file}')
        print('[0] Cancel')
        choice = IP.input_num_range(0, len(zips))
        if choice == 0:
            return None

        viewer = IP.ui.Viewer(self.dir['results'], zips[choice - 1])
        IP.ui.start_ui(viewer)
