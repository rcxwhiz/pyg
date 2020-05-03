import sys
import typing

from PyQt5.QtWidgets import QApplication, QFileDialog

app = None
filter_string = 'All Files (*);;Python Files (*.py);;Images (*.png *.jpg *.gif);;Text (*.txt);;CSV (*.csv)'


def check_app_active():
    global app
    if app is None:
        app = QApplication(sys.argv)


def get_directory(title: str = 'Open folder') -> str:
    check_app_active()
    to_return = QFileDialog.getExistingDirectory(None, title, "")
    return to_return


def get_file(title: str = 'Open file', filter_in: str = filter_string) -> str:
    check_app_active()
    to_return, selected_filter = QFileDialog.getOpenFileName(None, title, "", filter_in)
    return to_return


def get_files(title: str = 'Open files', filter_in: str = filter_string) -> typing.List[str]:
    check_app_active()
    to_return, selected_filter = QFileDialog.getOpenFileNames(None, title, "", filter_in)
    return to_return


def save_file(title: str = 'Save file', filter_in: str = filter_string) -> str:
    check_app_active()
    to_return, selected_filter = QFileDialog.getSaveFileName(None, title, "", filter_in)
    return to_return
