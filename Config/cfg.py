import configparser
import os
import sys
from os.path import join
from pathlib import Path

reader = configparser.ConfigParser()

try:
    reader.read(os.sep.join(sys.argv[0].split(os.sep)[:-1]) + os.sep + 'config.ini')
except FileNotFoundError:
    print(f"Couldn't find {join(os.getcwd(), 'config.ini')}")
    sys.exit()

show_warning = reader.getboolean('General', 'show_warning')
score_decimals = reader.getint('General', 'score_decimals')

base_directory = join(str(Path.home()), reader.get('File Structure', 'base_directory'))

max_threads = reader.getint('Runtime', 'max_threads')
max_out_lines = reader.getint('Runtime', 'max_out_lines')
max_program_time = reader.getint('Runtime', 'max_program_time')

max_threads = min(max_threads, 500)
if max_threads <= 0:
    max_threads = 500

if show_warning:
    original_file = open('config.ini', 'r', encoding='utf-8').read()
    open('config.ini', 'w', encoding='utf-8').write(
        original_file.replace('show_warning = true', 'show_warning = false'))
