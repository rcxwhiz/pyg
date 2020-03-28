import os
import shutil
import subprocess
import sys
import threading
from os.path import join

import InstructorProgram.main
from Config import cfg
from FileExecution import scripting
from FileExecution.security import security_check

error_msgs = {'unicode': '\n[GRADER] Unicode decode error',
              'input': '\n[GRADER] File terminated for using input',
              'long out': f'\n[GRADER] File output was cut off because it is longer than {cfg.max_out_lines} '
                          f'lines\nThe full output is located in the output file for this script '
                          f'(if it is not set to be deleted)'}


def run_key(assignment_dir):
    """
    This program will take the assignment directory and run stuff from key source to populate key output
    It will run stuff on threads and write files and ask for a grading criteria that needs to be saved
    """

    # get all test case dirctories
    test_cases = []
    for file in os.listdir(join(assignment_dir, 'test-cases')):
        if os.path.isdir(join(assignment_dir, 'test-cases', file)):
            test_cases.append(file)
    if len(test_cases) == 0:
        print(f'No test case directories found in {join(assignment_dir, "test-cases")}')
        print(f'If you want to run without any input files, just create an empty directory\n'
              f'inside of {join(assignment_dir, "test-cases")}')
        InstructorProgram.main.run()

    # get the key source file
    key_source_file = ''
    key_file_name = ''
    key_dir_files = os.listdir(join(assignment_dir, 'key-source'))
    for file in key_dir_files:
        if file.endswith('.py'):
            key_file_name = file
            key_source_file = join(assignment_dir, 'key-source', file)
            break
    if key_source_file == '':
        print(f'There was no python key file in: {join(assignment_dir, "key-source")}')
        InstructorProgram.main.run()

    # copy all test case files into temporary running directories
    run_pairs = []
    for test in test_cases:
        # make the temporary directory to test the key
        os.makedirs(join(assignment_dir, 'TEMP', f'key-{test}'))
        # copy data from test case directory
        for file in os.listdir(join(assignment_dir, 'test-cases', test)):
            shutil.copyfile(join(assignment_dir, 'test-cases', test, file),
                            join(assignment_dir, 'TEMP', f'key-{test}', file))

        shutil.copyfile(key_source_file, join(assignment_dir, 'TEMP', f'key-{test}', key_file_name))
        run_pairs.append([join(assignment_dir, 'TEMP', f'key-{test}', key_file_name),
                          join(assignment_dir, 'TEMP', f'key-{test}',
                               'output.txt')])

    # start threading crap here
    run_file_group(run_pairs)
    # move the generated stuff into the appropiate out folders
    out_file_list = []
    for test in test_cases:
        for file in os.listdir(join(assignment_dir, 'TEMP', f'key-{test}')):
            if file not in os.listdir(join(assignment_dir, 'test-cases', test)) and file not in os.listdir(
                    join(assignment_dir, 'key-source')):
                if not os.path.exists(join(assignment_dir, 'key-output', test)):
                    os.mkdir(join(assignment_dir, 'key-output', test))
                shutil.copyfile(join(assignment_dir, 'TEMP', f'key-{test}', file),
                                join(assignment_dir, 'key-output', test, file))
                out_file_list.append(join(assignment_dir, 'key-output', test, file))

    # remember to delete the whole TEMP directory when done
    shutil.rmtree(join(assignment_dir, 'TEMP'), ignore_errors=True)

    return out_file_list


def run_students(assignment_dir, download_dir):
    print('')


def run_file_group(run_pairs):
    """
    This function takes a list of 2 item lists which are source file and destination file
    It mostly manages the threading
    """

    num_to_run = len(run_pairs)
    ran = 0
    base_threads = threading.active_count()
    my_threads = []
    print(f'\n[Running {num_to_run} files on {cfg.max_threads} threads]')

    while ran < num_to_run:
        if threading.active_count() - base_threads < cfg.max_threads:
            new_thread = threading.Thread(target=run_file, args=(run_pairs[ran][0], run_pairs[ran][1]))
            new_thread.start()
            my_threads.append(new_thread)
            ran += 1
            if ran % 5 == 0 and ran != num_to_run:
                print(f'[{ran}/{num_to_run}]')
    for thread in my_threads:
        thread.join()

    print(f'[{ran}/{num_to_run}] Complete!')


def run_file(py_file, out_file):
    """
    Takes a source file and an output file and runs with checkoutput, then puts the results in the out file
    """

    temp_script_name = py_file[:-3] + '-MODIFIED.py'
    student_source_code = read_file(py_file)

    file_issues = security_check(student_source_code)
    if len(file_issues) > 0:
        open(out_file, 'w', encoding='utf-8').write(' + ILLEGAL CODE + \n' + '\n'.join(file_issues))
        return None

    full_script = (scripting.prepend + student_source_code + scripting.append)
    if cfg.max_program_time > 0:
        kill_time = cfg.max_program_time
    else:
        kill_time = sys.maxsize

    full_script = full_script.replace('TIME BEFORE KILL HERE', str(kill_time))
    open(temp_script_name, 'w', encoding='utf-8').write(full_script)

    result_string = subprocess.check_output(['python', temp_script_name], stderr=subprocess.STDOUT).decode('utf-8')

    print('Verify script output:')
    print(result_string)

    with open(out_file, 'w') as f:
        f.write(result_string)

    os.remove(temp_script_name)


def read_file(file):
    """
    Returns a string from loading a file
    """

    return open(file, 'rt', encoding='utf-8').read()
