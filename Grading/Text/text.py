import configparser
import os
import re
import typing
from os.path import join

from PYGUtils import *
from StudentReport import StudentReport

part_re = re.compile(r'([P|p][A|a][R|r][T|t][ ]*[:]?[-]*[ ]*)([a-zA-Z]|[0-9]+)')
part_output_re = re.compile(
    r'([P|p][A|a][R|r][T|t][ ]*[:]?[-]*[ ]*)([a-zA-Z]|[0-9]+)(.*)([P|p][A|a][R|r][T|t][ ]*[:]?[-]*[ ]*[a-zA-Z]|[0-9]+)?')


def find_parts(out_files: typing.List[str]) -> typing.List[typing.List[str]]:
    # make a list of parts using regex from a given out file (not string)
    found_parts = []
    hits = re.findall(part_re, open(out_files[0], 'r', encoding='utf-8').read())
    for hit in hits:
        found_parts.append([hit[0], hit[1]])
    return found_parts


def grade_students(assignment_dir: str, student_out_folders: typing.List[str]) -> typing.List[StudentReport]:
    student_grades = []
    error_str = f'\nERROR:\n' \
                f'There is a problem with the rubric at\n{join(assignment_dir, "rubric.ini")}\n' \
                f'If you have not filled it out, do that before automatically grading'
    try:
        criteria = Criteria(assignment_dir)
    except configparser.Error:
        print(error_str)
        return student_grades
    except ValueError:
        print(error_str)
        return student_grades

    for file in student_out_folders:
        student_id = tuple(file.split(os.sep)[-1].split('_')[:3])
        student_grades.append(StudentReport(student_id))
        criteria.grade(student_grades[-1], assignment_dir)

    return student_grades


class Criteria:

    def __init__(self, assignment_dir: str):
        reader = configparser.ConfigParser()
        reader.read(join(assignment_dir, 'rubric.ini'))
        self.total_points = reader.getint('Assignment', 'total_weight')
        self.test_cases = get_assignment_test_cases(assignment_dir)

        self.parts = {}
        for part in get_assignment_parts(assignment_dir):
            self.parts[part] = {}
        for test_case in self.test_cases:
            hits = []
            try:
                hits = re.findall(part_output_re, open(join(assignment_dir, 'key-output', test_case, 'output.txt'), 'r',
                                                       encoding='utf-8').read())
            except FileNotFoundError:
                print(
                    f'Issue loading key output for test case: {test_case} ({join(assignment_dir, "key-output", test_case, "output.txt")})')

            for hit in hits:
                self.parts[hit[0] + hit[1]][test_case] = re.sub(r'\n+', r'\n', re.sub(r' +', ' ', hit[2]))

    def grade(self, student_report: StudentReport, assignment_dir: str) -> None:
        for test_case in self.test_cases:
            student_report.test_cases[test_case] = {}
            for part in self.parts:
                student_report.test_cases[test_case][part] = False

            hits = []
            current_folder = join(assignment_dir,
                                  'TEMP',
                                  student_report.identifier(),
                                  test_case,
                                  f'{student_report.identifier()}-OUTPUT.txt')
            try:
                hits = re.findall(part_output_re, open(current_folder, 'r', encoding='utf-8').read())
            except FileNotFoundError:
                print(f'Issue loading {current_folder} for grading')

            for hit in hits:
                student_report.test_cases[test_case][hit[0] + hit[1]] = \
                    self.parts[hit[0] + hit[1]][test_case] == re.sub(r'\n+', r'\n', re.sub(r' +', ' ', hit[2]))
