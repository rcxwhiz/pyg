import os
import sys

from Config import cfg
import InstructorProgram as IP

if cfg.base_directory == 'default':
    if r'C:/Users/' in sys.argv[0]:
        s_path = os.path.normpath(sys.argv[0]).split(os.sep)

        new_base_dir = os.path.join(s_path[0], s_path[1], s_path[2], 'AutoGrader')
        print(f'[1] Use {new_base_dir} as base directory')
        print(f'[0] Don\'t use {new_base_dir} as base directory')
        change_config = IP.tools.input_num_range(0, 1)
        if change_config == 1:
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
