import os
import shutil
from os.path import join

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

    def check_full(self):
        return self.dirs.check_full(self.assignment_num)

    def generate_key_files(self):
        if len(os.listdir(self.dir['key-output'])) > 0:
            print('[1] Overwrite current key files')
            print('[0] Don\'t overwrite current key files')
            choice = IP.tools.input_num_range(0, 1)
            if choice == 1:
                shutil.rmtree(self.dir['key-output'], ignore_errors=True)
                os.mkdir(self.dir['key-output'])
            else:
                return None

        execute.run_key(self.dir['home'])

    def export_student_tester(self):
        print('export student tester')

    def grade_student_code(self):
        print('grade student code')

    def view_grading_report(self):
        print('view grading report')
