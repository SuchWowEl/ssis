
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
# from PySide6.QtWidgets import QTableView, QApplication, QMessageBox
# from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
# import pandasway_w_class as pd_obj
import csv
import re
import mysqltest as db
# from gui_V2 import Ui_Dialog
from gui_V2_copy import Ui_Dialog
import pandas as pd

# python -m PyQt6.uic.pyuic -o gui_V2_copy.py -x untitled2.ui


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
        if header == "student id":
            self.student_id_window(current_string, header)
        elif header != "warning":
            self.edit_window(current_string, header)
        else:
            self.confirm()

    def confirm(self):
        self.setWindowTitle("🤨")
        self.setFixedWidth(200)
        self.setFixedHeight(100)

        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel("Warning: Are you sure to delete?")

        ok_button = QtWidgets.QPushButton("OK")

        layout.addWidget(self.label)
        # layout.addWidget(self.combobox)
        layout.addWidget(ok_button)
        ok_button.clicked.connect(self.accept)
        self.setLayout(layout)

    def edit_window(self, current_string, header):
        # current_string = current_string.split()
        self.setWindowTitle(f"Change {header}")
        size = 475 if header in ["course", "name"] else 200
        self.setMinimumWidth(size)
        self.setFixedHeight(100)

        layout = QtWidgets.QHBoxLayout()
        # print(f"IT IS {current_string}")
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


class ChooserPopUp(QtWidgets.QDialog):
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
    radioButton_style = """
                    QRadioButton {
                        background-color:       rgb(39, 41, 50);
                        color:                  white;
                    }

                    QRadioButton::indicator {
                        width:                  10px;
                        height:                 10px;
                        border-radius:          7px;
                    }

                    QRadioButton::indicator:checked {
                        background-color:       rgb(216, 17, 89);
                        border:                 2px solid rgb(241, 234, 208);
                    }

                    QRadioButton::indicator:unchecked {
                        background-color:       rgb(39, 41, 50);
                        border:                 2px solid rgb(241, 234, 208);
                    }
                        """

    def __init__(self, parent, given_list, combo_string, header):
        super().__init__(parent)
        if header != "search":
            self.comboboxer(parent, given_list, combo_string, header)
        else:
            self.searcher(parent, given_list)

    def searcher(self, parent, given_list):
        self.setWindowTitle(f"Search 🔍🔍🔍")
        self.setFixedWidth(400)
        self.setFixedHeight(200)

        layout = QtWidgets.QVBoxLayout()

        self.id = QtWidgets.QLineEdit()
        self.id.setPlaceholderText("Enter id...")
        self.id.setMaxLength(9)
        self.id.setStyleSheet(self.lineedit_style)
        self.id.setFixedWidth(200)

        self.name = QtWidgets.QLineEdit()
        self.name.setPlaceholderText("Enter name...")
        self.name.setMaxLength(255)
        self.name.setStyleSheet(self.lineedit_style)

        # self.lists = [self.gender, self.year, db.list_of_courses()]
        self.gender = QtWidgets.QComboBox()
        self.gender.addItems(["not include gender"])
        self.gender.addItems(given_list[0])
        self.gender.setFixedWidth(200)

        self.year = QtWidgets.QComboBox()
        self.year.addItems(["not include year"])
        self.year.addItems(given_list[1])
        self.year.setFixedWidth(200)

        self.courses = QtWidgets.QComboBox()
        self.courses.addItems(["not include course"])
        self.courses.addItems(given_list[2])
        self.courses.setFixedWidth(200)

        radio_layout = QtWidgets.QHBoxLayout()
        self.button_group = QtWidgets.QButtonGroup()
        self.or_button = QtWidgets.QRadioButton("OR")
        self.and_button = QtWidgets.QRadioButton("AND")
        self.or_button.setStyleSheet(self.radioButton_style)
        self.and_button.setStyleSheet(self.radioButton_style)
        self.button_group.addButton(self.or_button)
        self.button_group.addButton(self.and_button)
        self.or_button.setChecked(True)
        radio_layout.addStretch(1)
        radio_layout.addWidget(self.or_button)
        radio_layout.addWidget(self.and_button)
        radio_layout.addStretch(1)

        layout.addStretch(1)
        layout.addWidget(self.id, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.name)
        layout.addWidget(self.gender, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.year, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.courses, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(1)
        layout.addLayout(radio_layout)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # layout.addWidget(self.combobox)

        ok_button = QtWidgets.QPushButton("OK")
        layout.addWidget(ok_button)
        ok_button.clicked.connect(self.array_setter)
        self.setLayout(layout)

    def array_setter(self):
        arr = [self.id.text().strip(), self.name.text().strip(), self.gender.currentText(
        ).strip(), self.year.currentText().strip(), self.courses.currentText().strip()]

        arr.append(self.or_button.text() if self.or_button.isChecked()
                   else self.and_button.text())

        for i in [2, 3, 4]:
            if "not include" in arr[i]:
                arr[i] = ""
        self.array = arr
        self.accept()

    def array_returner(self):
        return self.array

    def comboboxer(self, parent, given_list, combo_string, header):
        self.setWindowTitle(f"Choose new {header}")
        self.setFixedWidth(200)
        self.setFixedHeight(100)

        layout = QtWidgets.QVBoxLayout()
        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItems(given_list)
        self.combobox.setCurrentText(combo_string)
        layout.addWidget(self.combobox)
        ok_button = QtWidgets.QPushButton("OK")
        layout.addWidget(ok_button)
        ok_button.clicked.connect(self.accept)
        self.setLayout(layout)

    def get_selected_item(self):
        return self.combobox.currentText()


class Functions(Ui_Dialog):
    prevText = ""
    headers = []
    model = QtGui.QStandardItemModel()

    def table_to_QSIM(self, tuples):
        model = QtGui.QStandardItemModel()
        for row in range(len(tuples)):
            for column in range(len(tuples[0])):
                item = QtGui.QStandardItem(
                    str(tuples[row][column]))
                model.setItem(row, column, item)
                item.setEditable(False)
        return model

    def __init__(self, Dialog):
        super().__init__(Dialog)

        # self.studentsCSV = self.table_to_QSIM(db.table_for_students())
        # self.courseCSV = self.table_to_QSIM(db.table_for_courses())
        validator = QtGui.QIntValidator()
        self.lineEdit_id.setValidator(validator)
        self.lineEdit_id_2.setValidator(validator)

        # QtGui.QRegularExpressionValidator
        '''
        self.lineEdit_fname.setValidator(
            QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("[a-zA-Z]+")))
        self.lineEdit_mi.setValidator(
            QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("[a-zA-Z]+")))
        self.lineEdit_lname.setValidator(
            QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("[a-zA-Z]+")))
        '''

        self.studentModel = self.table_to_QSIM(db.table_for_students())
        self.courseModel = self.table_to_QSIM(db.table_for_courses())
        # self.pd_obj = pd_obj.pd_obj
        # self.studentsCSV = self.pd_obj.returnStudent()
        # self.courseCSV = self.pd_obj.returnCourse()
        # self.courseList = courseCSV['course'].tolist()
        # self.gui = Dialog
        # print(f"studentsCSV: \n{self.studentsCSV}")
        # print(f"courseCSV: \n{self.courseCSV}")
        # print(f"courseList: \n{self.courseList}")
        self.gender = ["Male", "Female", "Non-binary"]
        self.year = ["1st Year", "2nd Year", "3rd Year", "4th Year"]
        # self.courseList = db.list_of_courses()
        self.lists = [self.gender, self.year, db.list_of_courses()]

        self.modelSetter()
        self.setFunctions()

    def setFunctions(self):
        self.comboBox.insertItems(1, self.lists[2])
        self.GcomboBox.insertItems(1, self.gender)
        self.YcomboBox.insertItems(1, self.year)

        self.pushButton.clicked.connect(self.addClicked)
        self.pushButton_3.clicked.connect(self.search_table)
        self.deleteStudentButton.clicked.connect(
            lambda table: self.delete_entry("student id"))
        self.addCourseButton.clicked.connect(self.addCourseClicked)
        self.deleteCourseButton.clicked.connect(
            lambda table: self.delete_entry("course code"))

        self.studentTable.doubleClicked.connect(
            lambda index, table="students": self.trigger_popup(index, table))
        # self.studentTable.selectionModel().currentChanged.connect(self.on_student_selection_changed)
        self.courseTable.doubleClicked.connect(
            lambda index, table="courses": self.trigger_popup(index, table))
        # self.courseTable.selectionModel().currentChanged.connect(self.on_course_selection_changed)

        self.editEntryButton.clicked.connect(
            lambda table: self.updateModels("students"))
        self.editCourseButton.clicked.connect(
            lambda table: self.updateModels("courses"))

    def modelSetter(self):
        self.studentModel.blockSignals(True)
        self.headers = db.headers_of_table("students")
        self.studentModel.setHorizontalHeaderLabels(
            self.headers)
        self.studentTable.setModel(self.studentModel)
        for row in range(self.studentModel.rowCount()):
            for column in [2, 3, 4]:
                self.studentModel.itemFromIndex(
                    self.studentModel.index(row, column)).setEditable(False)
        self.studentModel.blockSignals(False)

        self.headers2 = db.headers_of_table("courses")
        self.courseModel.setHorizontalHeaderLabels(self.headers2)
        self.courseTable.setModel(self.courseModel)

    def addClicked(self):
        try:
            if any(id == "" or id.isspace() for id in [self.lineEdit_id.text(), self.lineEdit_id_2.text(), self.lineEdit_name.text()]):
                raise CustomException("Error: Please fill out all the fields")
            arrey = [f"{self.lineEdit_id.text().strip()}-{self.lineEdit_id_2.text()}", self.lineEdit_name.text().strip(), self.GcomboBox.currentText(
            ), self.YcomboBox.currentText(), self.comboBox.currentText()]
            if any(len(id) != 9 for id in arrey[:1]):
                raise CustomException(
                    "Error: Please fill out ID field properly")
            print(arrey)
            print(self.lists[2])
            db.add_row(arrey)
            num_rows = self.studentModel.rowCount()
            self.studentModel.insertRow(num_rows)
            self.studentModel.blockSignals(True)

            for column in range(self.studentModel.columnCount()):
                item = QtGui.QStandardItem(arrey[column])
                item.setEditable(False)
                self.studentModel.setItem(num_rows, column, item)

            self.studentModel.blockSignals(False)
        except Exception as e:
            var = CustomWarningBox(Dialog, text=str(e))
            var.exec()

    def search_table(self):
        search_dialog = ChooserPopUp(
            Dialog, self.lists, "none", "search")
        if search_dialog.exec() == 1:
            arr = search_dialog.array_returner()
            if any(item != "" for item in arr[0:5]):
                table_db = db.search_records(arr[0:5], arr[5])
                self.studentModel = self.table_to_QSIM(table_db)

                self.studentModel.blockSignals(True)
                self.studentModel.setHorizontalHeaderLabels(self.headers)
                self.studentTable.setModel(self.studentModel)

                self.studentModel.blockSignals(False)
                warning = CustomWarningBox(
                    Dialog, f"students: Refresh is successful")
                warning.exec()

    # unused
    def delete_rows(self, arr, header):
        currentModel = self.studentModel if header == "student id" else self.courseModel
        for row in arr:
            currentModel.removeRow(row)

    def student_id_in_course(self, primary_key):
        rows_to_remove = []
        for row in range(self.studentModel.rowCount()):
            # model.index(indx.row(), 0).data(0)
            if self.studentModel.index(row, 4).data(0) in primary_key:
                print(f"a student is chosen to be removed")
                rows_to_remove.append(row)
        rows_to_remove.sort(reverse=True)
        return rows_to_remove

    def delete_entry(self, table):
        dialog = EditPopUp(Dialog, "a", "warning")
        if dialog.exec() == 1:
            print("delete_entry IS CALLED and table is")
            print(table)
            selection_model = self.studentTable.selectionModel(
            ) if table == "student id" else self.courseTable.selectionModel()
            model = self.studentModel if table == "student id" else self.courseModel
            selected_indexes = selection_model.selectedIndexes()
            print(selected_indexes)
            if len(selected_indexes) != 0:
                rows_to_remove = []
                primary_key = []
                temp = -1
                for indx in selected_indexes:
                    if temp != indx.row():
                        rows_to_remove.append(indx.row())
                        primary_key.append(model.index(indx.row(), 0).data(0))
                        # to remove duplicate row indexes
                        temp = indx.row()
                print(f"rows_to_remove = {rows_to_remove}")
                rows_to_remove.sort(reverse=True)

                if table == "student id":
                    print("removing student entry/ies:")
                    # self.pd_obj.deleteEntry(rows_to_remove)
                    db.delete_rows(primary_key)
                else:
                    print("else:")
                    db.delete_course(primary_key)
                    # self.delete_rows(rows_to_remove, "course code")
                    rows_to_remove = self.student_id_in_course(primary_key)
                    self.lists[2] = db.list_of_courses()
                    self.updateModels("courses")

                    self.comboBox.clear()
                    self.comboBox.addItems(self.lists[2])
                self.updateModels("students")
                # self.delete_rows(rows_to_remove, "student id")

    def updateModels(self, table):
        if table == "students":
            table_db = db.table_for_students()
            self.studentModel = self.table_to_QSIM(table_db)
            model = self.studentModel
            header = self.headers
            tableview = self.studentTable
        else:
            table_db = db.table_for_courses()
            self.courseModel = self.table_to_QSIM(table_db)
            model = self.courseModel
            header = self.headers2
            tableview = self.courseTable
            self.lists[2] = db.list_of_courses()
            self.comboBox.clear()
            self.comboBox.addItems(self.lists[2])

        model.blockSignals(True)

        # header = db.headers_of_table(table)
        model.setHorizontalHeaderLabels(header)
        tableview.setModel(model)

        model.blockSignals(False)
        warning = CustomWarningBox(
            Dialog, f"{table}: Refresh is successful")
        warning.exec()

    def addCourseClicked(self):
        # condition1 = (not (self.addCourseLine_2.text() in self.lists[2]))
        condition2 = (
            all((line.text() != "" and not line.text().isspace()) for line in (self.addCourseLine, self.addCourseLine_2)))

        print(f"addCourseClicked condition: {condition2}")
        if condition2:
            try:
                arrey = [self.addCourseLine_2.text().strip(),
                         self.addCourseLine.text()]
                db.add_course(arrey)

                num_rows = self.courseModel.rowCount()
                self.courseModel.insertRow(num_rows)

                self.courseModel.blockSignals(True)

                for column in range(self.courseModel.columnCount()):
                    item = QtGui.QStandardItem(arrey[column])
                    self.courseModel.setItem(num_rows, column, item)

                self.courseModel.blockSignals(False)
                self.lists[2].append(arrey[0])
                # self.lists[2] = db.list_of_courses()
                # self.comboBox.clear()
                self.comboBox.addItem(arrey[0])
            except Exception as e:
                var = CustomWarningBox(Dialog, str(e))
                var.exec()
                # print(str(e))

    def trigger_popup(self, index, table):
        print(f"table == {table}")
        model = self.studentModel if table == "students" else self.courseModel
        etable = self.studentTable if table == "students" else self.courseTable
        header = model.headerData(
            index.column(), Qt.Orientation.Horizontal)
        current_text = index.data()

        dialog = ""
        if index.column() in [2, 3, 4]:
            dialog = ChooserPopUp(
                Dialog, self.lists[index.column()-2], index.data(), header)
        else:
            dialog = EditPopUp(Dialog, current_text, header)
        try:
            if dialog.exec() == 1:
                newInfo = dialog.get_selected_item()
                if newInfo == "":
                    raise CustomException("Error: Fix input")
                if index.data() != newInfo:
                    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                    idNumber = etable.model().index(
                        index.row(), 0).data()
                    print(
                        f"idNumber: {idNumber}, newInfo: {newInfo}, header: {header}")
                    db.edit_student(idNumber, newInfo, header) if table == "students" else db.edit_course(
                        idNumber, newInfo, header)
                    model.blockSignals(True)
                    item = QtGui.QStandardItem(newInfo)
                    model.setItem(
                        index.row(), index.column(), item)
                    item.setEditable(False)
                    model.blockSignals(False)
                    if header == "course code" and table == "courses":
                        self.lists[2] = db.list_of_courses()
                        self.updateModels("students")
                        # self.editCourseNameinSTable(current_text, newInfo)
        except Exception as e:
            print(str(e))
            var = CustomWarningBox(Dialog, str(e))
            var.exec()

    def editCourseNameinSTable(self, oldInfo, newInfo):
        print("\nupdateCourses called !!!")
        print(self.lists[2])
        print(self.studentModel.columnCount())

        # edit "course" in student Table when text in that row == oldInfo
        column = self.studentModel.columnCount()-1
        self.studentModel.blockSignals(True)
        for row in range(self.studentModel.rowCount()):
            index = self.studentModel.index(row, column)
            item = self.studentModel.itemFromIndex(index)
            print(item.text())
            if item.text() == oldInfo:
                item.setText(newInfo)
        self.studentModel.blockSignals(False)

        self.comboBox.clear()
        self.comboBox.addItems(self.lists[2])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    # gui = Ui_Dialog(Dialog)
    function_OBJ = Functions(Dialog)
    # ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
