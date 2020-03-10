import os
from Config import cfg
from FileExecution import scripting

error_msgs = {'unicode': '\n[GRADER] - Unicode decode error',
              'input': '\n[GRADER] - File terminated for using input',
              'long out': f'\n[GRADER] - File output was cut off because it is longer than {cfg.max_out_lines} '
                          f'lines\nThe full output is located in the output file for this script '
                          f'(if it is not set to be deleted)'}


def run_key(assignment_dir):
    print('')


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
