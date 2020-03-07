import configparser
import os
import sys

reader = configparser.ConfigParser()

os.chdir(os.path.dirname(sys.argv[0]))

reader.read('config.ini')

base_directory = reader.get('File Structure', 'base_directory')
