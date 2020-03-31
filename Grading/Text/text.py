import re

part_re = re.compile(r'([P|p][A|a][R|r][T|t][ ]*[:]?[-]*[ ]*)([a-zA-Z]|[0-9]+)')


def find_parts(out_files):
    # make a list of parts using regex from a given out file (not string)
    found_parts = []
    hits = re.findall(part_re, open(out_files[0], 'r', encoding='utf-8').read())
    for hit in hits:
        found_parts.append([hit[0], hit[1]])
    return found_parts


class Criteria:

    def __init__(self, parts_in, points_in, key_in):
        self.parts = parts_in
        self.total_points = points_in
        self.key_folder = key_in

    def grade(self, folder_in):
        print(f'Graded {folder_in}')
