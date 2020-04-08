from __future__ import annotations

import os
import shutil
import sys
from os.path import join

import InstructorProgram as IP
from Config import cfg


class Dirs:

    def __init__(self):
        # initialize and get the directories
        self.base = cfg.base_directory
        self.assignment_dirs = []
        self.required_assignment_dirs = ['key-source',
                                         'key-output',
                                         'student-source',
                                         'results',
                                         'test-cases']
        try:
            os.listdir(self.base)
        except FileNotFoundError:
            print(f'Program location: {self.base} not found')
            print(f'[1] Create {self.base}')
            print(f'[0] Do not create {self.base}')
            create_new_base = IP.input_num_range(0, 1)
            if create_new_base == 1:
                os.makedirs(self.base)
            else:
                print('Please change base directory in config.ini')
                sys.exit()

        self.update()

    def update(self):
        # decide if the directory is an assignment directory and if so add it to the list of assignment directories
        self.assignment_dirs = []
        for file in os.listdir(self.base):
            if os.path.isdir(join(self.base, file)) and f'{file}.assignment' in os.listdir(join(self.base, file)):
                self.assignment_dirs.append(file)

    def create_new(self, assignment_name):
        # tries to make the required directories in a new assignment directory
        if assignment_name not in os.listdir(self.base):
            try:
                os.mkdir(join(self.base, assignment_name))

                self.initialize_dirs(join(self.base, assignment_name))
                self.update()
            except FileNotFoundError:
                print('Cannot create a subdirectory')
        else:
            print(f'{assignment_name} already exists')

    def print_dirs(self):
        # prints out all the assignment directories that we have
        if len(self.assignment_dirs) == 0:
            print('None')
        else:
            for i, folder in enumerate(self.assignment_dirs):
                print(f'[{i + 1}] {folder}')

    def get_hw(self, assignment_index):
        self.initialize_dirs(join(self.base, self.assignment_dirs[assignment_index]))
        return IP.Assignment(self.assignment_dirs[assignment_index])

    def initialize_dirs(self, assignment_dir):
        # TODO here I am just writing something to mark this as an assigment directory
        with open(join(assignment_dir, f'{assignment_dir.split(os.sep)[-1]}.assignment'), 'w') as file:
            file.write('This file marks this directory as an assignment directory')

        # will check if an assignment directory has all the valid things in it and create them
        files = os.listdir(join(self.base, assignment_dir))

        if 'TEMP' in files:
            shutil.rmtree(join(self.base, assignment_dir, 'TEMP'), ignore_errors=True)

        for file in self.required_assignment_dirs:
            if file not in files:
                os.mkdir(join(self.base, assignment_dir, file))
