import re
from typing import List

part_re = re.compile(r'([P|p][A|a][R|r][T|t][ ]*[:]?[-]*[ ]*)([a-zA-Z]|[0-9]+)')


def find_parts(out_files: List[str]) -> List[List[str]]:
    # make a list of parts using regex from a given out file (not string)
    found_parts = []
    hits = re.findall(part_re, open(out_files[0], 'r', encoding='utf-8').read())
    for hit in hits:
        found_parts.append([hit[0], hit[1]])
    return found_parts


class Criteria:

    def __init__(self, parts_in, points_in, key_in, pp_in):
        self.parts = parts_in
        self.total_points = points_in
        self.key_folder = key_in
        self.progressive_points = pp_in

    def grade(self, out_files):
        # TODO I should probably load the key outputs a strings here
        # TODO here I am going to make an excel report with xlrd of what people got on what parts

        # TODO first make a dict with the ids and outputs
        # outputs will be a dict as well with the testcase and the output
        # raise an issue here if there are duplicates

        print('Done grading')

    def grade_student(self, files):
        print('grade student')

    def write_xlsx_report(self):
        print('Made report')
