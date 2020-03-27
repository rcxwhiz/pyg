import sys
from os.path import join
from pathlib import Path

from Config import cfg


def change_config(new_name):
    f = open('config.ini', 'r')
    config_text = f.read().replace('default', new_name)
    f.close()
    f = open('config.ini', 'w')
    f.write(config_text)
    f.close()
    print('Please restart the program')
    sys.exit()


if cfg.base_directory == 'default':

    new_base_dir = join(str(Path.home()), 'AutoGrader')
    if not Path.exists(Path(new_base_dir)):
        print(f'[1] Create {new_base_dir} and use as base directory')
        print(f'[0] Exit and change config.ini')
        choice = -1
        answer = -1
        while answer < 0 or answer > 1:
            try:
                answer = int(input('\rOption: '))
            except ValueError:
                continue
        if choice == 1:
            change_config(new_base_dir)
            print('Please restart the program')

        sys.exit()
    else:
        change_config(new_base_dir)

import InstructorProgram as IP
IP.run()
