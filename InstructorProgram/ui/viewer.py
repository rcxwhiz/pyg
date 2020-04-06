from zipfile import ZipFile
from os.path import join


class Viewer:

    def __init__(self, folder, zip_file):
        ZipFile(join(folder, zip_file)).extractall()

        student_info = {}

        self.student_name_id_list = []
        self.test_cases = []
        self.assignment_name = ''

    def next_name_id(self):
        return 0

    def prev_name_id(self):
        return 0

    def
