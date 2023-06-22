# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
# from PySide6.QtWidgets import QTableView, QApplication, QMessageBox
# from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from pandasway_w_class import pd_obj
import csv
import pandas as pd
import os
from gui_v1_2 import UI_Dialog

script_dir = os.path.dirname(os.path.abspath(__file__))

studentsFile = os.path.join(script_dir, 'students.csv')
courseFile = os.path.join(script_dir, 'course.csv')
tableStyleSheet = """
            QTableView {
                background-color: rgb(39, 41, 50);
                color: white;
                border: 2px solid rgb(130, 132, 137);
            }
            QHeaderView::section {
                background-color: rgb(39, 41, 50);
                color: white;
            }
            QTableCornerButton::section {
                background-color: rgb(39, 41, 50);
                color: white;
            }
            QHeaderView::section:hover {
                background-color: rgb(241, 234, 208);
                color: rgb(39, 41, 50);
            }
            QTableView::item:hover {
                background-color: rgb(241, 234, 208);
                color: rgb(39, 41, 50);
            }
            QTableView::item:selected {
                background-color: rgb(245, 241, 224);
                color: rgb(39, 41, 50);
            }
        """


class CustomException(Exception):
    pass


class CustomWarningBox(QtWidgets.QDialog):
    def __init__(self, parent, text):
        super().__init__(parent)
        self.setWindowTitle(f"Warning!")
        self.setMinimumWidth(300)
        self.setMinimumHeight(100)

        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel(text)
        self.setLayout(layout)
        layout.addWidget(self.label)

        # self.exec()


class EditPopUp(QtWidgets.QDialog):
    lineedit_style = """
                    QLineEdit {
                        border-style: none;
                        border-bottom-style: solid;
                        border-width: 0 0 2px 0;
                        border-color: rgb(71, 115, 154);
                        color: white;
                        background-color: transparent;
                    }
                    """

    def __init__(self, parent, current_string, header):
        super().__init__(parent)
        if header == "id":
            self.student_id_window(current_string, header)
        else:
            self.edit_window(current_string, header)

    def edit_window(self, current_string, header):
        # current_string = current_string.split()
        self.setWindowTitle(f"Change {header}")
        size = 475 if header in ["course", "name"] else 200
        self.setMinimumWidth(size)
        self.setFixedHeight(100)

        layout = QtWidgets.QHBoxLayout()
        print(f"IT IS {current_string}")
        self.line = QtWidgets.QLineEdit(current_string)
        self.line.setMaxLength(255)
        self.line.setStyleSheet(self.lineedit_style)
        ok_button = QtWidgets.QPushButton("OK")

        layout.addWidget(self.line)
        layout.addWidget(ok_button)
        ok_button.clicked.connect(self.line_returner)
        self.setLayout(layout)

    def student_id_window(self, current_string, header):
        self.setWindowTitle("Change ID number")
        self.setFixedWidth(200)
        self.setFixedHeight(100)
        whew = self.lineedit_style

        layout = QtWidgets.QHBoxLayout()
        self.id = QtWidgets.QLineEdit(current_string[:4])
        self.id.setStyleSheet(self.lineedit_style)
        self.dash = QtWidgets.QLabel("-")
        self.id2 = QtWidgets.QLineEdit(current_string[5:])
        self.id2.setStyleSheet(self.lineedit_style)
        self.id.setMaxLength(4)
        self.id2.setMaxLength(4)

        validator = QtGui.QIntValidator()
        self.id.setValidator(validator)
        self.id2.setValidator(validator)

        ok_button = QtWidgets.QPushButton("OK")

        layout.addWidget(self.id)
        layout.addWidget(self.dash)
        layout.addWidget(self.id2)
        # layout.addWidget(self.combobox)
        layout.addWidget(ok_button)
        ok_button.clicked.connect(self.id_returner)
        self.setLayout(layout)

    def line_returner(self):
        try:
            if self.line.text() != "" or not self.line.text().isspace():
                self.new_input = self.line.text().strip()
                self.accept()
            else:
                self.new_input = ""
                raise CustomException("Error: fix input")
        except Exception as e:
            self.accept()

    def id_returner(self):
        try:
            if all(id != "" and len(id) == 4 for id in [self.id.text(), self.id2.text()]):
                self.new_input = f"{self.id.text()}-{self.id2.text()}"
                self.accept()
            else:
                self.new_input = ""
                raise CustomException("Error: fix input")
        except Exception as e:
            self.accept()

    def get_selected_item(self):
        return self.new_input
        # return self.combobox.currentText()


class CoursePopUp(QtWidgets.QDialog):
    def __init__(self, parent, courseList, combo_string):
        super().__init__(parent)
        self.setWindowTitle("Choose new Course")
        self.setFixedWidth(200)
        self.setFixedHeight(100)

        layout = QtWidgets.QVBoxLayout()
        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItems(courseList)
        self.combobox.setCurrentText(combo_string)
        layout.addWidget(self.combobox)
        ok_button = QtWidgets.QPushButton("OK")
        layout.addWidget(ok_button)
        ok_button.clicked.connect(self.accept)
        self.setLayout(layout)

    def get_selected_item(self):
        return self.combobox.currentText()


class Functional(UI_Dialog):
    # table_object = pd_obj()
    prevText = ""
    headers = []
    studentModel = QtGui.QStandardItemModel()
    courseModel = QtGui.QStandardItemModel()
    studentsCSV = pd.read_csv(studentsFile)
    courseCSV = pd.read_csv(courseFile)
    courseList = courseCSV['course'].tolist()
    model = QtGui.QStandardItemModel()

    def __init__(self, Dialog):
        super().__init__(Dialog)
        self.setupUI()

    def setFunctions(self):
        self.pushButton.clicked.connect(self.addClicked)
        self.pushButton_3.clicked.connect(self.search_table)
        self.deleteStudentButton.clicked.connect(
            lambda header: self.delete_entry("not course"))
        self.deleteCourseButton.clicked.connect(
            lambda header: self.delete_entry("course"))
        self.addCourseButton.clicked.connect(self.addCourseClicked)
        # self.studentModel.itemChanged.connect(lambda item, header="": self.edit_cell(item, self.studentModel.headerData(item.column(), Qt.Orientation.Horizontal)))
        # self.studentTable.selectionModel().currentChanged.connect(self.on_student_selection_changed)
        # self.studentTable.clicked.connect(self.set_prev_text)
        self.studentTable.doubleClicked.connect(
            lambda index, table="students": self.trigger_popup(index, table))
        # self.courseModel.itemChanged.connect(lambda item, header="": self.edit_cell(item, self.courseModel.headerData(item.column(), Qt.Orientation.Horizontal)))
        # self.courseTable.selectionModel().currentChanged.connect(self.on_course_selection_changed)
        self.courseTable.doubleClicked.connect(
            lambda index, table="courses": self.trigger_popup(index, table))

        self.tabWidget.currentChanged.connect(self.handle_tab_changed)

    def trigger_popup(self, index, table):
        print(f"table == {table}")
        row = index.row()
        columnNumber = index.column()
        # column = self.headers[columnNumber]
        # new_text = item.text()
        # print(f"new text is {new_text}")
        previous_text = index.data()
        model = self.studentModel if table == "students" else self.courseModel
        header = model.headerData(
            index.column(), Qt.Orientation.Horizontal)

        dialog = ""
        if index.column() == 2:
            dialog = CoursePopUp(Dialog, self.courseList, previous_text)
        else:
            dialog = EditPopUp(Dialog, previous_text, header)
        try:
            if dialog.exec() == 1:
                newInfo = dialog.get_selected_item()
                print(newInfo)
                if newInfo != "" and not newInfo.isspace():
                    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

                    inCourse = not pd_obj.notInCSV(newInfo, "course", 0)
                    inStudent = not pd_obj.notInCSV(newInfo, header, 1)
                    if not inCourse and table == "courses":
                        print("editCourse")
                        print(f"{previous_text},{newInfo}")
                        pd_obj.editCourse(previous_text, newInfo)
                        self.courseModel.blockSignals(True)
                        self.courseModel.item(
                            row, columnNumber).setText(newInfo)
                        self.courseModel.item(
                            row, columnNumber).setEditable(False)
                        self.courseModel.blockSignals(False)

                        self.courseList[row] = self.prevText = newInfo
                        self.editCourseNameinSTable(
                            oldInfo=previous_text, newInfo=newInfo)
                    elif inCourse and table == "courses":
                        raise CustomException(
                            f"Error: \"{newInfo}\" is duplicate")
                    else:
                        print("editEntry")
                        print(f"{previous_text},{newInfo}, {header}")
                        if header == "name" or (header == "id" and not inStudent):
                            # pd_obj.editEntry(previous_text,newInfo, header)
                            idNum = self.studentModel.index(row, 1).data(0)
                            pd_obj.editEntry2(idNum, newInfo, header)
                        elif header == "id" and inStudent:
                            raise CustomException(
                                f"Error: \"{newInfo}\" is duplicate")
                        else:
                            idNum = self.studentModel.index(row, 1).data(0)
                            print(f"idNum: {idNum}, newCourse: {newInfo}")
                            pd_obj.editEntryCourse(idNum, newInfo)
                        self.studentModel.blockSignals(True)
                        self.studentModel.item(
                            row, columnNumber).setText(newInfo)
                        self.studentModel.item(
                            row, columnNumber).setEditable(False)
                        self.studentModel.blockSignals(False)
                else:
                    raise CustomException("Error: Please fix input")
        except Exception as e:
            print(str(e))
            var = CustomWarningBox(Dialog, str(e))
            var.exec()

    def addClicked(self):
        # if self.lineEdit_name.text() and self.lineEdit_id.text() and self.lineEdit_id_2.text() and self.comboBox.currentText():
        try:
            if all(text and not text.isspace() for text in [self.lineEdit_name.text(), self.lineEdit_id.text(), self.lineEdit_id_2.text(), self.comboBox.currentText()]):
                if all(len(id) == 4 for id in [self.lineEdit_id.text(), self.lineEdit_id_2.text()]):
                    arrey = [self.lineEdit_name.text().strip(), f"{self.lineEdit_id.text()}-{self.lineEdit_id_2.text()}",
                             self.comboBox.currentText()]
                    print(arrey)
                    if (not pd_obj.studentInCSV(arrey)):
                        pd_obj.addEntry(arrey)

                        num_rows = self.studentModel.rowCount()

                        self.studentModel.insertRow(num_rows)

                        for column in range(self.studentModel.columnCount()):
                            self.prevText = arrey[column]
                            item = QtGui.QStandardItem(arrey[column])
                            self.studentModel.setItem(num_rows, column, item)
                            item.setEditable(False)
            else:
                raise CustomException("Please fix input")
        except Exception as e:
            print(str(e))
            var = CustomWarningBox(Dialog, str(e))
            var.exec()

    def search_table(self):
        search_string = self.lineEdit_name_3.text()
        # self.studentsCSV = pd.read_csv(studentsFile)
        for row in range(self.studentModel.rowCount()):
            match_found = False
            for column in range(self.studentModel.columnCount()-1):
                print(
                    f"KOBEEE {self.studentModel.index(row, column).data(0)}")
                temp = self.studentModel.index(row, column).data(0)
                if temp and search_string.lower() in temp.strip().lower():
                    match_found = True
                    break
            if match_found:
                self.studentTable.setRowHidden(row, False)
            else:
                self.studentTable.setRowHidden(row, True)

    def delete_rows(self, arr, header):
        currentModel = self.studentModel if header != "course" else self.courseModel
        for row in arr:
            currentModel.removeRow(row)

    def delete_entry(self, header):
        print("delete_entry IS CALLED and header is")
        print(header)
        selection_model = self.studentTable.selectionModel(
        ) if header != "course" else self.courseTable.selectionModel()

        selected_indexes = selection_model.selectedIndexes()

        rows_to_remove = []
        for index in selected_indexes:
            rows_to_remove.append(index.row())
        rows_to_remove.sort(reverse=True)
        if header != "course":
            print("if header != 'course':")
            pd_obj.deleteEntry(rows_to_remove)
        else:
            print("else:")
            self.delete_rows(rows_to_remove, "course")
            for index in rows_to_remove:
                print(
                    f"index in rows is {index}")
                self.courseList.pop(index)
            # get rows_to_remove for studentTable
            rows_to_remove = sorted(
                pd_obj.deleteCourse(rows_to_remove), reverse=True)
            self.comboBox.clear()
            self.comboBox.addItems(self.courseList)
        self.delete_rows(rows_to_remove, "not course")
        print(self.courseList)

    def modelSetter(self):
        self.headers = list(self.studentsCSV.columns)
        self.studentModel.setHorizontalHeaderLabels(
            self.studentsCSV.columns)

        self.headers2 = list(self.courseCSV.columns)
        self.courseModel.setHorizontalHeaderLabels(self.courseCSV.columns)

    def setModelStudent(self, pdCSV):
        model = QtGui.QStandardItemModel()
        for row in range(len(pdCSV)):
            for column in range(len(pdCSV.columns)):
                item = QtGui.QStandardItem(
                    str(pdCSV.iloc[row, column]))
                model.setItem(row, column, item)
                item.setEditable(False)
        return model

    def addCourseClicked(self):
        print(
            f"{not (self.addCourseLine.text().strip() is None or not self.addCourseLine.text().strip())}")
        print(f"{self.addCourseLine.text().strip() in self.courseList}")
        if not (self.addCourseLine.text().strip() in self.courseList) and not (self.addCourseLine.text().strip() is None or not self.addCourseLine.text()):
            pd_obj.addCourse(self.addCourseLine.text().strip())
            self.courseModel.appendRow(
                [QtGui.QStandardItem(self.addCourseLine.text().strip())])

            index = self.courseModel.index(
                self.courseModel.rowCount()-1, self.courseModel.columnCount()-1)
            print(
                f"row: {self.courseModel.rowCount()-1}, column: {self.courseModel.columnCount()-1}")
            self.courseModel.itemFromIndex(index).setEditable(False)

            self.courseList.append(self.addCourseLine.text())
            self.comboBox.addItem(self.addCourseLine.text())

    def setSModel(self):
        # self.studentsCSV = pd.read_csv(studentsFile)
        # self.courseCSV = pd.read_csv(courseFile)
        self.courseList = self.courseCSV['course'].tolist()

        self.studentModel = self.setModelStudent(self.studentsCSV)
        self.courseModel = self.setModelStudent(self.courseCSV)
        self.modelSetter()

    def handle_tab_changed(self, index):
        index = not index
        elementNum = 0 if index else 0
        # i = 0 for widget in self.tabWidget.widget(index).children(): print(f"{widget.objectName()}: {i}") i += 1 print("-------------------------------")
        previous_tableview = self.tabWidget.widget(index).children()[0]

        previous_tableview.selectionModel().clearSelection()
        previous_tableview.clearFocus()
        self.lineEdit_name.setFocus() if index else self.addCourseLine.setFocus()

    def setComposeTable(self):
        self.setSModel()
        self.comboBox.addItems(self.courseList)

        self.studentTable.setModel(self.studentModel)
        self.studentTable.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.courseTable.setModel(self.courseModel)
        self.courseTable.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.studentTable.setStyleSheet(tableStyleSheet)
        self.courseTable.setStyleSheet(tableStyleSheet)

    def editCourseNameinSTable(self, oldInfo, newInfo):
        print("updateCourses called !!!")
        print(self.courseList)

        # edit "course" in student Table when text in that row == oldInfo
        column = 2
        for row in range(self.studentModel.rowCount()):
            index = self.studentModel.index(row, column)
            item = self.studentModel.itemFromIndex(index)
            if item.text() == oldInfo:
                item.setText(newInfo)

        self.comboBox.clear()
        self.comboBox.addItems(self.courseList)

    def set_prev_text(self, index):
        if index.column() == 2:
            # self.prevText = index.data()
            dialog = CoursePopUp(Dialog, self.courseList, index.data())
            if dialog.exec() == 1:
                newCourse = dialog.get_selected_item()
                if index.data() != newCourse:
                    idNumber = self.studentTable.model().index(
                        index.row(), index.column()-1).data()
                    pd_obj.editEntryCourse(idNumber, newCourse)
                    self.studentModel.blockSignals(True)
                    item = QtGui.QStandardItem(newCourse)
                    self.studentModel.setItem(index.row(), 2, item)
                    self.studentModel.blockSignals(False)

    def setupUI(self):
        self.setComposeTable()
        self.setFunctions()

        validator = QtGui.QIntValidator()
        self.lineEdit_id.setValidator(validator)
        self.lineEdit_id_2.setValidator(validator)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    # gui = Ui_Dialog(Dialog)
    function_OBJ = Functional(Dialog)
    # ui.setupUI(Dialog)
    Dialog.show()
    sys.exit(app.exec())
