from __future__ import annotations

import os
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
        self.update()

    def update(self):
        self.assignment_dirs = []
        for file in os.listdir(self.base):
            if os.path.isdir(join(self.base, file)) and 'sag-info.txt' in os.listdir(join(self.base, file)):
                self.assignment_dirs.append(file)

    def create_new(self, assignment_name):
        if assignment_name not in os.listdir(self.base):
            os.mkdir(join(self.base, assignment_name))
            f = open(join(self.base, assignment_name, 'sag-info.txt'), 'w')
            f.write('test')
            f.close()
            self.update()
        else:
            print(f'{assignment_name} already exists')

    def print_dirs(self):
        if len(self.assignment_dirs) == 0:
            print('None')
        else:
            for i, folder in enumerate(self.assignment_dirs):
                print(f'[{i + 1}] - {folder}')
