import os
import shutil
from os.path import join
from zipfile import ZipFile

import xlrd


class Viewer:

    def __init__(self, folder: str, zip_file: str):
        self.assignment_name = ''
        self.student_info = {}

        self.key_source = ''
        self.key_outputs = {}

        self.index = 0
        self.student_name_id_list = []

        self.test_case_index = 0
        self.test_cases = []

        with ZipFile(join(folder, zip_file), 'r') as zipp:
            zipp.extractall(path=join(folder, 'TEMP'))

        found_xlsx = False
        for file in os.listdir(join(folder, 'TEMP')):
            if file == 'report.xlsx':
                self.get_data_from_xlsx(join(folder, 'TEMP', 'report.xlsx'))
                found_xlsx = True
            elif os.path.isdir(join(folder, 'TEMP', file)):
                self.student_name_id_list.append(file)
                if file not in self.student_info.keys():
                    self.student_info[file] = {}
                for sub_file in os.listdir(join(folder, 'TEMP', file)):
                    if sub_file.endswith('.py'):
                        self.student_info[file]['source'] = open(join(folder, 'TEMP', file, sub_file), 'rt',
                                                                 encoding='utf-8').read()
                    elif sub_file.endswith('.txt'):
                        if 'output' not in self.student_info[file].keys():
                            self.student_info[file]['output'] = {}
                        # TODO I need to figure out how I am saving the txt files and load those here
                        # self.student_info[file]['output'][]

        if not found_xlsx:
            raise FileNotFoundError

        shutil.rmtree(join(folder, 'TEMP'))

        # TODO num test cases and students
        """
        The way this is going to work is I am going to load the data purely from the excel sheet and the given files
        If there is an issue loading the files I am going to do a try except and just print that it was expected that
        I would get whatever file and then move on
        
        I will... raise a file not found error that will be caught in assignment.py and stop the ui from launching
        """

    def get_data_from_xlsx(self, full_path: str) -> None:
        wb = xlrd.open_workbook(full_path)
        sheet = wb.sheet_by_name('Grades')
        num_parts = 0
        num_tests = 0

        i = 4
        while True:
            if sheet.cell_value(0, i) != '':
                num_parts += 1
                i += 1
            else:
                break

        i = 5
        while True:
            if sheet.cell_value(0, i) != '':
                num_tests += 1
                self.test_cases.append(sheet.cell_value(0, 5 + i))
                i += 1
            else:
                break

        i = 1
        while True:
            if sheet.cell_value(i, 0) != '':
                current_name = '_'.join([sheet.cell_value(i, 0), sheet.cell_value(i, 1), sheet.cell_value(i, 2)])
                if current_name not in self.student_info.keys():
                    self.student_info[current_name] = {}
                self.student_info[current_name]['total score'] = sheet.cell_value(i, 3)
                for j in range(num_tests):
                    self.student_info[current_name]['pass fail'][j] = sheet.cell_value(i, 4 + num_parts + j)
                i += 1
            else:
                break

    def next_name_id(self) -> str:
        if self.index == len(self.student_name_id_list):
            return self.formatter(0)
        else:
            return self.formatter(self.index + 1)

    def prev_name_id(self) -> str:
        return self.formatter(self.index - 1)

    def current_name_id(self) -> str:
        name_id = self.student_name_id_list[self.index]
        parts = name_id.split('_')
        last = parts[0]
        first = parts[1]
        student_id = parts[2]
        content = f'{first} {last} ({self.index + 1}/{len(self.student_name_id_list)})\n'
        content += f'{student_id} - Total score: {self.student_info[name_id]["total score"]}'
        return content

    def current_pass_fail(self) -> str:
        return self.student_info[self.student_name_id_list[self.index]]['pass fail'][self.test_case_index]

    def formatter(self, index: int) -> str:
        parts = self.student_name_id_list[index].split('_')
        return f'{parts[1]} {parts[0]} - {parts[2]}'

    def increment(self) -> None:
        if self.index == len(self.student_name_id_list):
            self.index = 0
        else:
            self.index += 1

    def decrement(self) -> None:
        if self.index == 0:
            self.index = len(self.student_name_id_list)
        else:
            self.index -= 1

    def set_student_index(self, index: int) -> None:
        self.index = index

    def set_test_case_index(self, index: int) -> None:
        self.test_case_index = index

    def student_source_code(self) -> str:
        return self.student_info[self.student_name_id_list[self.index]]['source']

    def student_output(self) -> str:
        return self.student_info[self.student_name_id_list[self.index]]['output'][self.test_case_index]

    def student_case_score(self) -> str:
        return self.student_info[self.student_name_id_list[self.index]]['score'][self.test_case_index]

    def student_total_score(self) -> str:
        return self.student_info[self.student_name_id_list[self.index]]['total score']

    def key_output(self) -> str:
        return self.key_outputs[self.test_case_index]

    def test_case_name(self) -> str:
        return self.test_cases[self.test_case_index]
