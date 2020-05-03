import configparser
import os
import shutil
import sys
from os.path import join
from pathlib import Path

reader = configparser.ConfigParser()

try:
    reader.read(join(os.getcwd(), os.path.dirname(sys.argv[0]), 'config.ini'))
except FileNotFoundError:
    print(f"Couldn't find {join(os.getcwd(), os.path.dirname(sys.argv[0]), 'config.ini')}")
    print('Creating default config file...')
    shutil.copyfile(join(os.getcwd(), os.path.dirname(sys.argv[0]), 'Config', 'default_config.ini'),
                    join(os.getcwd(), os.path.dirname(sys.argv[0]), 'config.ini'))
    reader.read(join(os.getcwd(), os.path.dirname(sys.argv[0]), 'config.ini'))

# General
show_warning = reader.getboolean('General', 'show_warning')
score_decimals = reader.getint('General', 'score_decimals')

# File Structure
base_directory = join(str(Path.home()), reader.get('File Structure', 'base_directory'))

# Runtime
max_threads = reader.getint('Runtime', 'max_threads')
max_out_lines = reader.getint('Runtime', 'max_out_lines')
max_program_time = reader.getint('Runtime', 'max_program_time')

max_threads = min(max_threads, 500)
if max_threads <= 0:
    max_threads = 500

# Security/Restrictions
max_code_lines = reader.getint('Security/Restrictions', 'max_code_lines')
phrase_blacklist = reader.get('Security/Restrictions', 'phrase_blacklist').split('\n')
phrase_blacklist[:] = [_ for _ in phrase_blacklist if _ != '']
package_whitelist = reader.get('Security/Restrictions', 'package_whitelist').split('\n')
package_whitelist[:] = [_ for _ in package_whitelist if _ != '']
function_blacklist = reader.get('Security/Restrictions', 'function_blacklist').split('\n')
function_blacklist[:] = [_ for _ in function_blacklist if _ != '']

if show_warning:
    original_file = open('config.ini', 'r', encoding='utf-8').read()
    open('config.ini', 'w', encoding='utf-8').write(
        original_file.replace('show_warning = true', 'show_warning = false'))
