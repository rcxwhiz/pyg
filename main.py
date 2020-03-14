import sys
from os.path import join
from pathlib import Path

from Config import cfg

if cfg.base_directory == 'default':

    new_base_dir = join(str(Path.home()), 'AutoGrader')
    print(f'[1] Create {new_base_dir} and use as base directory')
    print(f'[0] Exit and change config.ini')
    change_config = -1
    answer = -1
    while answer < 0 or answer > 1:
        try:
            answer = int(input('\rOption: '))
        except ValueError:
            continue
    if change_config == 1:
        f = open('config.ini', 'r')
        config_text = f.read().replace('default', new_base_dir)
        f.close()
        f = open('config.ini', 'w')
        f.write(config_text)
        f.close()
        print('Please restart the program')
        sys.exit()

    sys.exit()

import InstructorProgram as IP

IP.run()
