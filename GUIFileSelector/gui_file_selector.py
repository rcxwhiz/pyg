import sys
import typing

from PyQt5.QtWidgets import QApplication, QFileDialog

app = None
filter_string = 'All Files (*);;Python Files (*.py);;Images (*.png *.jpg *.gif);;Text (*.txt);;CSV (*.csv)'
all_files_filter_string = 'All Files (*)'


def check_app_active():
    global app
    if app is None:
        app = QApplication(sys.argv)


def get_directory(title: str = 'Open folder', starting_dir: str = '') -> str:
    check_app_active()
    to_return = QFileDialog.getExistingDirectory(None, title, starting_dir)
    return to_return


def get_file(title: str = 'Open file', filter_in: str = all_files_filter_string, starting_dir: str = '') -> str:
    check_app_active()
    to_return, selected_filter = QFileDialog.getOpenFileName(None, title, starting_dir, filter_in)
    return to_return


def get_files(title: str = 'Open files', filter_in: str = all_files_filter_string, starting_dir: str = '') -> \
typing.List[str]:
    check_app_active()
    to_return, selected_filter = QFileDialog.getOpenFileNames(None, title, starting_dir, filter_in)
    return to_return


def save_file(title: str = 'Save file', filter_in: str = all_files_filter_string, starting_dir: str = '') -> str:
    check_app_active()
    to_return, selected_filter = QFileDialog.getSaveFileName(None, title, starting_dir, filter_in)
    return to_return


if __name__ == '__main__':
    folder = get_directory()
    choice = input()
    print('done')
