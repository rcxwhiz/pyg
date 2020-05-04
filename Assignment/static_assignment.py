import os
from os.path import join

import Assignment.assignment_helper as helper
import GUIFileSelector as gfs
import Grading
import PYGUtils as putil
import UI
from FileExecution import execution
from Viewer import Viewer


def generate_key_files(assignment_dir: str) -> None:
    if not helper.can_run_key(assignment_dir):
        return None

    if not helper.can_run_key(assignment_dir):
        return None

    out_file_list = execution.run_key(assignment_dir)

    for file in out_file_list:
        if ' + ILLEGAL CODE + ' in execution.read_file(file):
            print(execution.read_file(file))
            print('\nGrading criteria cannot be created')
            return None

    assignment_parts = Grading.Text.text.find_parts(out_file_list)
    if not assignment_parts:
        assignment_parts = ['default']

    name = assignment_dir.split(os.sep)[-1]
    if name == '':
        name = assignment_dir.split(os.sep)[-2]
    putil.generate_blank_rubric(assignment_parts, join(assignment_dir, 'rubric.ini'), name)
    print(f'Please fill out {join(assignment_dir, "rubric.ini")} before automatically grading file')


def export_tester(assignment_dir: str) -> None:
    print('export tester')


def auto_grade(assignment_dir: str) -> None:
    print('Choose a folder of student source code')
    source_dir = gfs.get_directory('Select Student Source Dir', assignment_dir)
    if source_dir == '':
        return None

    student_ids, types_found = helper.get_ids_from_files(source_dir)
    helper.makedir(assignment_dir, student_ids)
    types_to_move = helper.get_types_to_move(types_found)
    helper.move_student_files(assignment_dir, source_dir, types_to_move)
    out_files = execution.run_students(assignment_dir)
    grades = Grading.Text.text.grade_students(assignment_dir, out_files)
    helper.generate_grade_report(assignment_dir, grades)
    helper.zip_report(assignment_dir)


def manual_grade(assignment_dir: str) -> None:
    print('manual grade')


def view_grade_report(assignment_dir: str) -> None:
    print('Choose a report to view')
    report = gfs.get_file('Choose Assignment Report Zip', 'Zip Files (*.zip)', join(assignment_dir, 'results'))
    if report == '':
        return None

    viewer = Viewer(join(assignment_dir, 'results'), report)
    UI.start_ui(viewer)
