from __future__ import annotations

import os
import sys
from os.path import join
from typing import Optional

from Config import cfg


class DirsMeta(type):
    _instance: Optional[Dirs] = None

    def __call__(self) -> Dirs:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Dirs(metaclass=DirsMeta):
    def __init__(self):
        self.base = cfg.base_directory
        self.assignment_dirs = []
        self.required_dirs = ['key-source',
                              'key-output',
                              'student-source',
                              'results',
                              'test-cases']
        try:
            os.listdir(self.base)
        except FileNotFoundError:
            create_new_base = input(f'Create {self.base}? (y/n) ').lower()
            if create_new_base == 'y':
                os.makedirs(self.base)
            else:
                print('Please change base directory in config.ini')
                sys.exit()

        self.update()

    def update(self):
        self.assignment_dirs = []
        for file in os.listdir(self.base):
            if os.path.isdir(join(self.base, file)) and 'sag-info.txt' in os.listdir(join(self.base, file)):
                self.assignment_dirs.append(file)

    def create_new(self, assignment_name):
        if assignment_name not in os.listdir(self.base):
            try:
                os.mkdir(join(self.base, assignment_name))
                f = open(join(self.base, assignment_name, 'sag-info.txt'), 'w')
                f.write('test')
                f.close()

                for file in self.required_dirs:
                    os.mkdir(join(self.base, assignment_name, file))

                self.update()
            except FileNotFoundError:
                print('Do not create subdirectories')
        else:
            print(f'{assignment_name} already exists')

    def print_dirs(self):
        if len(self.assignment_dirs) == 0:
            print('None')
        else:
            for i, folder in enumerate(self.assignment_dirs):
                print(f'[{i + 1}] - {folder}')

    def check_full(self, assignment_num):
        issues = []
        assignment_dir = self.assignment_dirs[assignment_num]
        files = os.listdir(join(self.base, assignment_dir))

        for file in self.required_dirs:
            if file not in files:
                issues.append(f'{file} not found in {join(self.base, assignment_dir)}')
        if len(issues) > 0:
            return issues

        need_to_not_be_empty = ['key-source',
                                'student-source',
                                'test-cases']

        for directory in need_to_not_be_empty:
            if not os.listdir(join(self.base, assignment_dir, directory)):
                issues.append(f'Dir {directory} is empty')

        return issues
