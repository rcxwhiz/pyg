# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InstructorProgram/ui/grade_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


import sys

from PyQt5 import QtCore, QtWidgets

from Viewer import Viewer


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QtWidgets.QMainWindow, viewer: Viewer) -> None:
        self.viewer = viewer

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 839)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.full_student_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.full_student_dropdown.setObjectName("full_student_dropdown")
        self.horizontalLayout_2.addWidget(self.full_student_dropdown)
        self.prev_student_button = QtWidgets.QPushButton(self.centralwidget)
        self.prev_student_button.setObjectName("prev_student_button")
        self.horizontalLayout_2.addWidget(self.prev_student_button)
        self.next_student_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_student_button.setObjectName("next_student_button")
        self.horizontalLayout_2.addWidget(self.next_student_button)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.key_file_label = QtWidgets.QLabel(self.centralwidget)
        self.key_file_label.setObjectName("key_file_label")
        self.verticalLayout_3.addWidget(self.key_file_label)
        self.key_source_viewer = QtWidgets.QTextBrowser(self.centralwidget)
        self.key_source_viewer.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.key_source_viewer.setObjectName("key_source_viewer")
        self.verticalLayout_3.addWidget(self.key_source_viewer)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.test_case_changer = QtWidgets.QSpinBox(self.centralwidget)
        self.test_case_changer.setObjectName("test_case_changer")
        self.horizontalLayout_3.addWidget(self.test_case_changer)
        self.test_case_label = QtWidgets.QLabel(self.centralwidget)
        self.test_case_label.setObjectName("test_case_label")
        self.horizontalLayout_3.addWidget(self.test_case_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.key_output_viewer = QtWidgets.QTextBrowser(self.centralwidget)
        self.key_output_viewer.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.key_output_viewer.setObjectName("key_output_viewer")
        self.verticalLayout_3.addWidget(self.key_output_viewer)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.student_label = QtWidgets.QLabel(self.centralwidget)
        self.student_label.setObjectName("student_label")
        self.verticalLayout_4.addWidget(self.student_label)
        self.student_source_viewer = QtWidgets.QTextBrowser(self.centralwidget)
        self.student_source_viewer.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.student_source_viewer.setObjectName("student_source_viewer")
        self.verticalLayout_4.addWidget(self.student_source_viewer)
        self.test_case_pass_fail_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_case_pass_fail_label.sizePolicy().hasHeightForWidth())
        self.test_case_pass_fail_label.setSizePolicy(sizePolicy)
        self.test_case_pass_fail_label.setMinimumSize(QtCore.QSize(0, 28))
        self.test_case_pass_fail_label.setObjectName("test_case_pass_fail_label")
        self.verticalLayout_4.addWidget(self.test_case_pass_fail_label)
        self.student_output_viewer = QtWidgets.QTextBrowser(self.centralwidget)
        self.student_output_viewer.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.student_output_viewer.setObjectName("student_output_viewer")
        self.verticalLayout_4.addWidget(self.student_output_viewer)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.link_buttons()
        self.update_ui()

    def retranslateUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", self.viewer.assignment_name))
        for i in range(len(self.viewer.student_name_id_list)):
            self.full_student_dropdown.setItemText(i, _translate("MainWindow", self.viewer.formatter(i)))

        self.prev_student_button.setText(_translate("MainWindow", "Previous Student - Name - ID"))
        self.next_student_button.setText(_translate("MainWindow", "Next Student - Name - ID"))
        self.key_file_label.setText(_translate("MainWindow", "Key Source \n"
                                                             f"{self.viewer.assignment_name}"))
        self.test_case_label.setText(_translate("MainWindow", "Test Case 1"))
        self.student_label.setText(_translate("MainWindow", "Student Name (num/total)\n"
                                                            "ID - Total Score"))
        self.test_case_pass_fail_label.setText(_translate("MainWindow", "Passed / Failed"))
        self.key_source_viewer.setText(self.viewer.key_source)

    def link_buttons(self) -> None:
        self.prev_student_button.clicked.connect(self.move_page_backward)
        self.next_student_button.clicked.connect(self.move_page_forward)
        self.test_case_changer.setMinimum(1)
        self.test_case_changer.setMaximum(len(self.viewer.test_cases))
        self.test_case_changer.valueChanged.connect(self.update_test_case)
        self.full_student_dropdown.currentIndexChanged.connect(self.change_student_id)

    def change_student_id(self) -> None:
        self.viewer.set_student_index(self.full_student_dropdown.currentIndex())
        self.update_ui()

    def move_page_backward(self) -> None:
        self.viewer.decrement()
        self.update_ui()

    def move_page_forward(self) -> None:
        self.viewer.increment()
        self.update_ui()

    def update_test_case(self) -> None:
        self.viewer.set_test_case_index(self.test_case_changer.value())
        self.update_ui()

    def update_ui(self) -> None:
        self.prev_student_button.setText(self.viewer.prev_name_id())
        self.next_student_button.setText(self.viewer.next_name_id())

        self.test_case_label.setText(self.viewer.test_case_name())

        self.student_label.setText(self.viewer.current_name_id())

        self.test_case_pass_fail_label.setText(self.viewer.current_pass_fail())

        self.key_output_viewer.setText(self.viewer.key_output())

        self.student_source_viewer.setText(self.viewer.student_source_code())
        self.student_output_viewer.setText(self.viewer.student_output())

        self.full_student_dropdown.setCurrentIndex(self.viewer.index)


def start_ui(viewer: Viewer) -> None:
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, viewer)
    MainWindow.show()
    app.exec_()
