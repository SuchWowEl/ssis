
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
# from PySide6.QtWidgets import QTableView, QApplication, QMessageBox
# from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
import pandasway_w_class as pd_obj
import csv
import mysqltest as db
from gui_V2 import Ui_Dialog
import pandas as pd

# python -m PyQt6.uic.pyuic -o gui_V2_copy.py -x untitled2.ui


class CustomException(Exception):
    pass


class ChooserPopUp(QtWidgets.QDialog):
    def __init__(self, parent, given_list, combo_string, header):
        super().__init__(parent)
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
                if column == 4:
                    item.setEditable(False)
        return model

    def __init__(self, Dialog):
        super().__init__(Dialog)

        # self.studentsCSV = self.table_to_QSIM(db.table_for_students())
        # self.courseCSV = self.table_to_QSIM(db.table_for_courses())

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
        '''
        csv_file = open('course.csv', newline='')
        reader = csv.reader(csv_file)
        next(reader)
        items = [row[0] for row in reader]
        self.comboBox.insertItems(1, items)
        '''
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

        self.studentModel.itemChanged.connect(
            lambda item, table="students": self.edit_cell(item, self.studentModel.headerData(item.column(), Qt.Orientation.Horizontal), table))
        self.studentTable.selectionModel().currentChanged.connect(
            self.on_student_selection_changed)
        self.studentTable.clicked.connect(self.trigger_popup)
        self.courseModel.itemChanged.connect(
            lambda item, table="courses": self.edit_cell(item, self.courseModel.headerData(item.column(), Qt.Orientation.Horizontal), table))
        self.courseTable.selectionModel().currentChanged.connect(
            self.on_course_selection_changed)
        self.tabWidget.currentChanged.connect(self.handle_tab_changed)

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
        if self.lineEdit_name.text() and self.lineEdit_id.text() and self.comboBox.currentText():
            arrey = [self.lineEdit_id.text(), self.lineEdit_name.text(), self.GcomboBox.currentText(
            ), self.YcomboBox.currentText(), self.comboBox.currentText()]
            print(arrey)
            print(db.duplicate_checker("student id", arrey[0], "students"))
            print(self.lists[2])
            if db.duplicate_checker("student id", arrey[0], "students") is None:
                # ----------------------------------------------------------------------------------------------------------------------------------------------
                db.add_row(arrey)
                num_rows = self.studentModel.rowCount()
                self.studentModel.insertRow(num_rows)
                self.studentModel.blockSignals(True)

                for column in range(self.studentModel.columnCount()):
                    self.prevText = arrey[column]
                    item = QtGui.QStandardItem(arrey[column])
                    self.studentModel.setItem(num_rows, column, item)
                    if column in [2, 3, 4]:
                        self.studentModel.itemFromIndex(
                            self.studentModel.index(num_rows, column)).setEditable(False)
                self.studentModel.sort(0, Qt.SortOrder.AscendingOrder)

                self.studentModel.blockSignals(False)
# ----------------------------------------------------------------------------------------------------------------------------------------------

    def search_table(self):
        if self.pushButton_3.text() is not None:
            search_string = self.lineEdit_name_3.text()
            # self.studentsCSV = pd.read_csv(studentsFile)
            for row in range(self.studentModel.rowCount()):
                match_found = False
                for column in range(self.studentModel.columnCount()):
                    print(
                        f"KOBEEE {self.studentModel.index(row, column).data(0)}")
                    temp = self.studentModel.index(row, column).data(0)
                    if temp is not None and search_string.lower() in temp.strip().lower():
                        match_found = True
                        break
                if match_found:
                    self.studentTable.setRowHidden(row, False)
                else:
                    self.studentTable.setRowHidden(row, True)

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
        print("delete_entry IS CALLED and table is")
        print(table)
        selection_model = self.studentTable.selectionModel(
        ) if table == "student id" else self.courseTable.selectionModel()
        model = self.studentModel if table == "student id" else self.courseModel
        selected_indexes = selection_model.selectedIndexes()

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
            self.delete_rows(rows_to_remove, "course code")
            rows_to_remove = self.student_id_in_course(primary_key)

            model.sort(1, Qt.SortOrder.AscendingOrder)
            self.lists[2] = db.list_of_courses()

            self.comboBox.clear()
            self.comboBox.addItems(self.lists[2])
        self.delete_rows(rows_to_remove, "student id")

    # not needed

    def updateModels(self, table):
        if table == "students":
            table_db = db.table_for_students()
            model = self.studentModel
            header = self.headers
            tableview = self.studentTable
        else:
            table_db = db.table_for_courses()
            model = self.courseModel
            header = self.headers2
            tableview = self.courseTable

        model.blockSignals(True)

        model = self.table_to_QSIM(table_db)
        header = db.headers_of_table(table)
        model.setHorizontalHeaderLabels(header)
        tableview.setModel(model)

        model.blockSignals(False)

    def addCourseClicked(self):
        condition1 = (not (self.addCourseCodeLine.text() in self.lists[2]))
        condition2 = (
            all((line.text() != "" and not line.text().isspace()) for line in (self.addCourseLine, self.addCourseCodeLine)))

        #    if (new_text != ""):
        #        if not new_text.isspace() and db.duplicate_checker(column, new_text, table) is None:

        print(f"addCourseClicked condition: {condition2}")
        if condition2:
            try:
                if db.duplicate_checker("course code", self.addCourseCodeLine.text(), "courses"):
                    raise CustomException("Course Code is duplicate")
                elif db.duplicate_checker("course", self.addCourseLine.text(), "courses"):
                    raise CustomException("Course is duplicate")
                arrey = [self.addCourseCodeLine.text(),
                         self.addCourseLine.text()]
                db.add_course(arrey)
                # self.courseModel.sort(1, Qt.SortOrder.AscendingOrder)

                num_rows = self.courseModel.rowCount()
                self.courseModel.insertRow(num_rows)

                self.courseModel.blockSignals(True)

                for column in range(self.courseModel.columnCount()):
                    self.prevText = arrey[column]
                    item = QtGui.QStandardItem(arrey[column])
                    self.courseModel.setItem(num_rows, column, item)
                self.courseModel.sort(1, Qt.SortOrder.AscendingOrder)

                self.courseModel.blockSignals(False)
                self.lists[2] = db.list_of_courses()
                self.comboBox.clear()
                self.comboBox.addItems(self.lists[2])
                # self.updateModels("courses")

                '''
                self.courseModel.appendRow(
                    [QtGui.QStandardItem(self.addCourseLine.text())], [QtGui.QStandardItem(self.addCourseLine.text())])
                self.courseList.append(self.addCourseLine.text())
                self.comboBox.addItem(self.addCourseLine.text())
                print(self.courseModel.indexFromItem(
                    self.courseModel.index(2, 1)).data())
                '''
            except Exception as e:
                print(str(e))

    def edit_cell(self, item, column, table):
        print(f"\nediting {table}: ")
        row = item.row()
        columnNumber = item.column()
        new_text = item.text()

        model = self.studentModel if table == "students" else self.courseModel
        key_value = model.index(row, 0).data(0)
        previous_text = self.prevText  # if self.prevText != "" else new_text
        # print(f"conditional is: {not new_text.isspace() and db.duplicate_checker(column, new_text, table) is None}")

        try:
            if (new_text != ""):
                if not new_text.isspace() and db.duplicate_checker(column, new_text, table) is None:
                    key = previous_text if column == "course code" or column == "student id" else key_value
                    db.edit_course(key, new_text, column) if table == "courses" else db.edit_student(
                        key, new_text, column)
                    if key == previous_text:
                        if table == "students":
                            model.sort(
                                0, Qt.SortOrder.AscendingOrder)
                        if table == "courses":
                            print(f"new_text: {new_text}")
                            self.lists[2] = db.list_of_courses()
                            # self.courseList[row] = self.prevText = new_text
                            self.editCourseNameinSTable(
                                previous_text, new_text)
                    if column == "course":
                        model.sort(1, Qt.SortOrder.AscendingOrder)
                    self.prevText = new_text
                else:
                    raise CustomException(
                        "Exception: Data is only space/s or a duplicate")
            else:
                raise CustomException("Exception: Data is blank")
        except Exception as e:
            print(str(e))
            model.blockSignals(True)
            model.itemFromIndex(model.index(
                row, columnNumber)).setText(previous_text)
            model.blockSignals(False)

    def on_student_selection_changed(self, current_index, previous_index):
        column = current_index.column()
        row = current_index.row()
        self.prevText = self.studentModel.data(current_index)
        print(
            f"Selected cell({column}, {row}): '{self.prevText}'")

    def trigger_popup(self, index):
        if index.column() in [2, 3, 4]:
            # self.prevText = index.data()
            list_to_give = self.lists[index.column()-2]
            current_text = index.data()
            header = self.studentModel.headerData(
                index.column(), Qt.Orientation.Horizontal)
            dialog = ChooserPopUp(Dialog, list_to_give, index.data(), header)
            if dialog.exec() == 1:
                newInfo = dialog.get_selected_item()
                if index.data() != newInfo:
                    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                    idNumber = self.studentTable.model().index(
                        index.row(), 0).data()
                    # self.pd_obj.editEntryCourse(idNumber, newInfo)
                    db.edit_student(idNumber, newInfo, header)
                    self.studentModel.blockSignals(True)
                    item = QtGui.QStandardItem(newInfo)
                    self.studentModel.setItem(
                        index.row(), index.column(), item)
                    self.studentModel.blockSignals(False)

    def on_course_selection_changed(self, current_index, previous_index):
        column = current_index.column()
        row = current_index.row()
        self.prevText = self.courseModel.data(current_index)
        print(f"Selected cell({column}, {row}): '{self.prevText}'")

    def handle_tab_changed(self, index):
        # False == student, True == course
        index = not index
        # elementNum = 4 if index else 0
        # i = 0 for widget in self.tabWidget.widget(index).children(): print(f"{widget.objectName()}: {i}") i += 1 print("-------------------------------")
        previous_tableview = self.tabWidget.widget(index).children()[0]

        previous_tableview.selectionModel().clearSelection()
        previous_tableview.clearFocus()
        self.lineEdit_name.setFocus() if index else self.addCourseCodeLine.setFocus()

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
