from os.path import join
from zipfile import ZipFile


class Viewer:

    def __init__(self, folder, zip_file):
        ZipFile(join(folder, zip_file)).extractall()

        self.assignment_name = ''
        self.student_info = []

        self.key_source = ''
        self.key_outputs = {}

        self.index = 0
        self.student_name_id_list = []

        self.test_case_index = 0
        self.test_cases = []

        # TODO load all this crap
        # TODO num test cases and students

    def next_name_id(self):
        if self.index == len(self.student_name_id_list):
            return self.formatter(0)
        else:
            return self.formatter(self.index + 1)

    def prev_name_id(self):
        return self.formatter(self.index - 1)

    def current_name_id(self):
        name_id = self.student_name_id_list[self.index]
        parts = name_id.split('_')
        last = parts[0]
        first = parts[1]
        student_id = parts[2]
        content = f'{first} {last} ({self.index + 1}/{len(self.student_name_id_list)})\n'
        content += f'{student_id} - Total score: {self.student_info[name_id]["total score"]}'
        return content

    def current_pass_fail(self):
        if self.student_info[self.student_name_id_list[self.index]]['pass fail'][self.test_case_index]:
            return 'Passed'
        else:
            return 'Failed'

    def formatter(self, index):
        parts = self.student_name_id_list[index].split('_')
        return f'{parts[1]} {parts[0]} - {parts[2]}'

    def increment(self):
        if self.index == len(self.student_name_id_list):
            self.index = 0
        else:
            self.index += 1

    def decrement(self):
        if self.index == 0:
            self.index = len(self.student_name_id_list)
        else:
            self.index -= 1

    def set_student_index(self, index):
        self.index = index

    def set_test_case_index(self, index):
        self.test_case_index = index

    def student_source_code(self):
        return self.student_info[self.student_name_id_list[self.index]]['source']

    def student_output(self):
        return self.student_info[self.student_name_id_list[self.index]]['output'][self.test_case_index]

    def student_case_score(self):
        return self.student_info[self.student_name_id_list[self.index]]['score'][self.test_case_index]

    def student_total_score(self):
        return self.student_info[self.student_name_id_list[self.index]]['total score']

    def key_output(self):
        return self.key_outputs[self.test_case_index]

    def test_case_name(self):
        return self.test_cases[self.test_case_index]
