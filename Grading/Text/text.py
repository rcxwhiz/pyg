import configparser
import os
import re
import typing
from os.path import join

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
    criteria = Criteria(assignment_dir)
    student_grades = []

    for file in student_out_folders:
        student_id = tuple(file.split(os.sep)[-1].split('_')[:3])
        student_grades.append(StudentReport(student_id))
        criteria.grade(student_grades[-1], assignment_dir)

    return student_grades


class Criteria:

    def __init__(self, assignment_dir: str):
        reader = configparser.ConfigParser()
        reader.read(join(assignment_dir, 'ruberic.ini'))
        self.total_points = reader.getint('Assignment', 'total_weight')
        self.test_cases = os.listdir(join(assignment_dir, 'test-cases'))

        self.parts = {}
        for test_case in self.test_cases:
            hits = []
            try:
                hits = re.findall(part_output_re, open(join(assignment_dir, test_case), 'r', encoding='utf-8').read())
            except FileNotFoundError:
                print(f'Issue loading key output for test case: {test_case}!')

            for hit in hits:
                self.parts[hit[0] + hit[1]][test_case] = re.sub(r'\n+', r'\n', re.sub(r' +', ' ', hit[2]))

    def grade(self, student_report: StudentReport, assignment_dir: str) -> None:
        for test_case in self.test_cases:
            hits = []
            current_folder = join(assignment_dir, student_report.id(), f'{student_report.id()}-{test_case}-OUTPUT.txt')
            try:
                hits = re.findall(part_output_re, open(current_folder, 'r', encoding='utf-8').read())
            except FileNotFoundError:
                print(f'Issue loading {current_folder} for grading')

            student_report.test_cases[test_case][hits[0] + hits[1]] = \
                self.parts[hits[0] + hits[1]][test_case] == re.sub(r'\n+', r'\n', re.sub(r' +', ' ', hits[2]))
