import configparser
import os
import sys

reader = configparser.ConfigParser()

os.chdir(os.path.dirname(sys.argv[0]))

reader.read('config.ini')

base_directory = reader.get('File Structure', 'base_directory')

# TODO there should be a variable check here to make sure config options are in range (esp. threads)
