import os
from os.path import join
from Config import cfg
from FileExecution import scripting
import shutil
import threading


error_msgs = {'unicode': '\n[GRADER] - Unicode decode error',
              'input': '\n[GRADER] - File terminated for using input',
              'long out': f'\n[GRADER] - File output was cut off because it is longer than {cfg.max_out_lines} '
                          f'lines\nThe full output is located in the output file for this script '
                          f'(if it is not set to be deleted)'}


def run_key(assignment_dir):
    # get all test case dirctories
    test_cases = []
    for file in os.listdir(join(assignment_dir, 'test-cases')):
        if os.path.isdir(file):
            test_cases.append(file)

    run_pairs = []
    # copy all test case files into temporary running directories
    for test in test_cases:
        # make the temporary directory to test the key
        os.makedirs(join(assignment_dir, 'TEMP', f'key-{test}'))
        # copy data from test case directory
        for file in os.listdir(join(assignment_dir, 'test-cases', test)):
            shutil.copyfile(join(assignment_dir, 'test-cases', test, file), join(assignment_dir, 'TEMP', f'key-{test}', file))
        run_pairs.append([])

    # start threading crap here
    num_to_run = len(test_cases)
    ran = 0
    base_threads = threading.active_count()
    while ran < num_to_run:
        if threading.active_count() - base_threads < cfg.max_threads:
            run_file()

    # remember to delete the whole TEMP directory when done


def run_students(assignment_dir, download_dir):
    print('')


def run_file(py_file, out_file):
    temp_script_name = py_file[:-3] + '-MODIFIED.py'
    student_source_code = read_file(py_file)

    if 'input(' in student_source_code or 'input (' in student_source_code:
        open(out_file, 'w').write(error_msgs['input'])
        return None

    full_script = (scripting.prepend + student_source_code + scripting.append)
    full_script = full_script.replace('TIME BEFORE KILL HERE', str(cfg.max_program_time))
    open(temp_script_name, 'w', encoding='utf-8').write(full_script)

    os.system(f'python "{temp_script_name}" > "{out_file}" 2>&1')
    os.remove(temp_script_name)


def read_file(file):
    return open(file, 'rt', encoding='utf-8').read()
