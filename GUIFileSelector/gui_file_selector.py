import sys
import typing

from PyQt5.QtWidgets import QApplication, QFileDialog

app = QApplication(sys.argv)
filter_string = 'All Files (*);;Python Files (*.py);;Images (*.png *.jpg *.gif);;Text (*.txt);;CSV (*.csv)'


def get_directory(title: str = 'Open folder') -> str:
    to_return = QFileDialog.getExistingDirectory(None, title, "")
    return to_return


def get_file(title: str = 'Open file', filter_in: str = filter_string) -> str:
    to_return, selected_filter = QFileDialog.getOpenFileName(None, title, "", filter_in)
    return to_return


def get_files(title: str = 'Open files', filter_in: str = filter_string) -> typing.List[str]:
    to_return, selected_filter = QFileDialog.getOpenFileNames(None, title, "", filter_in)
    return to_return


def save_file(title: str = 'Save file', filter_in: str = filter_string) -> str:
    to_return, selected_filter = QFileDialog.getSaveFileName(None, title, "", filter_in)
    return to_return
