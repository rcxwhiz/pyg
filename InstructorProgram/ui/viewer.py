from zipfile import ZipFile
from os.path import join


class Viewer:

    def __init__(self, folder, zip_file):
        ZipFile(join(folder, zip_file)).extractall()

        self.assignment_name = ''
        self.student_info = {}

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
        return self.formatter(self.index)

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
        return # TODO I don't know how I'm sotring the test cases (name or index)
