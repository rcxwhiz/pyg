import configparser
import os
import sys
from pathlib import Path
from os.path import join

reader = configparser.ConfigParser()

os.chdir(os.path.dirname(sys.argv[0]))

reader.read('config.ini')

base_directory = join(str(Path.home()), reader.get('File Structure', 'base_directory'))

reweight = reader.getint('Grading', 'reweight')

max_threads = reader.getint('Runtime', 'max_threads')
max_out_lines = reader.getint('Runtime', 'max_out_lines')
max_program_time = reader.getint('Runtime', 'max_program_time')

max_threads = min(max_threads, 500)
if max_threads == 0:
    max_threads = 500
if max_threads < 1:
    print('Max threads in config.ini < 1, exiting...')
    sys.exit()
