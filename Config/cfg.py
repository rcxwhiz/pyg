import configparser
import os
import sys
from os.path import join
from pathlib import Path

reader = configparser.ConfigParser()

try:
    reader.read('config.ini')
except FileNotFoundError:
    print(f"Couldn't find {join(os.getcwd(), 'config.ini')}")
    sys.exit(input('Press enter to exit...'))

show_warning = reader.getboolean('General', 'show_warning')
if show_warning:
    reader.set('General', 'show_warning', 'false')

base_directory = join(str(Path.home()), reader.get('File Structure', 'base_directory'))

max_threads = reader.getint('Runtime', 'max_threads')
max_out_lines = reader.getint('Runtime', 'max_out_lines')
max_program_time = reader.getint('Runtime', 'max_program_time')

max_threads = min(max_threads, 500)
if max_threads <= 0:
    max_threads = 500
