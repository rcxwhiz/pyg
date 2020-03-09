import os
import sys

from Config import cfg

if cfg.base_directory == 'default':
    if r'C:/Users/' in sys.argv[0]:
        s_path = os.path.normpath(sys.argv[0]).split(os.sep)

        new_base_dir = os.path.join(s_path[0], s_path[1], s_path[2], 'AutoGrader')
        change_config = input(f'Use {new_base_dir} as base direcetory? (y/n) ').lower()
        if change_config == 'y':
            f = open('config.ini', 'r')
            config_text = f.read().replace('default', new_base_dir)
            f.close()
            f = open('config.ini', 'w')
            f.write(config_text)
            f.close()
            print('Please restart')
            sys.exit()

    print('Please change base directory in config.ini')
    sys.exit()

import InstructorProgram

InstructorProgram.run()
