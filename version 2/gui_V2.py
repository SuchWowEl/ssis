# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

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


class Ui_Dialog(object):

    def __init__(self, Dialog):
        self.setupUi(Dialog)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(882, 761)
        Dialog.setMinimumSize(QtCore.QSize(882, 761))
        Dialog.setMaximumSize(QtCore.QSize(882, 761))
        Dialog.setStyleSheet("background-color: rgb(39, 41, 50);\n"
                             "selection-color: rgb(255, 255, 255);\n"
                             "color: rgb(182, 194, 217);")
        self.tabWidget = QtWidgets.QTabWidget(parent=Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 861, 741))
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(9999, 9999))
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
                                     "                border: 2px solid rgb(130, 132, 137);\n"
                                     "            }\n"
                                     "            QTabBar::tab {\n"
                                     "                background-color: rgb(99, 101, 105);\n"
                                     "                color: rgb(245, 241, 224);\n"
                                     "            }\n"
                                     "            QTabBar::tab:selected {\n"
                                     "                background-color: rgb(130, 132, 137);\n"
                                     "            }\n"
                                     "")
        self.tabWidget.setObjectName("tabWidget")
        self.studentTab = QtWidgets.QWidget()
        self.studentTab.setObjectName("studentTab")
        self.studentTable = QtWidgets.QTableView(parent=self.studentTab)
        self.studentTable.setGeometry(QtCore.QRect(40, 240, 781, 441))
        self.studentTable.setStyleSheet(tableStyleSheet)
        self.studentTable.setObjectName("studentTable")
        self.studentTable.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.editEntryButton = QtWidgets.QPushButton(parent=self.studentTab)
        self.editEntryButton.setGeometry(QtCore.QRect(620, 190, 81, 31))
        self.editEntryButton.setStyleSheet("border-radius: 5px;\n"
                                           "color: rgb(241, 234, 208);\n"
                                           "border :2px solid rgb(216, 17, 89);")
        self.editEntryButton.setObjectName("editEntryButton")
        self.deleteStudentButton = QtWidgets.QPushButton(
            parent=self.studentTab)
        self.deleteStudentButton.setGeometry(QtCore.QRect(720, 190, 101, 31))
        self.deleteStudentButton.setStyleSheet("border-radius: 5px;\n"
                                               "color: rgb(241, 234, 208);\n"
                                               "border :2px solid rgb(216, 17, 89);")
        self.deleteStudentButton.setObjectName("deleteStudentButton")
        self.label_9 = QtWidgets.QLabel(parent=self.studentTab)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(245, 241, 224);")
        self.label_9.setObjectName("label_9")
        self.lineEdit_name_3 = QtWidgets.QLineEdit(parent=self.studentTab)
        self.lineEdit_name_3.setGeometry(QtCore.QRect(130, 190, 321, 31))
        self.lineEdit_name_3.setStyleSheet("border-style: none;\n"
                                           "border-bottom-style: solid;\n"
                                           "border-width: 0 0 2px 0;\n"
                                           "border-color: rgb(71, 115, 154);\n"
                                           "color: white;\n"
                                           "background-color: transparent;")
        self.lineEdit_name_3.setInputMask("")
        self.lineEdit_name_3.setText("")
        self.lineEdit_name_3.setObjectName("lineEdit_name_3")
        self.label_8 = QtWidgets.QLabel(parent=self.studentTab)
        self.label_8.setGeometry(QtCore.QRect(30, 190, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(245, 241, 224);")
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.studentTab)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 190, 61, 31))
        self.pushButton_3.setStyleSheet("border-radius: 5px ;\n"
                                        "color: rgb(241, 234, 208);\n"
                                        "border :2px solid rgb(216, 17, 89);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.studentTab)
        self.groupBox_4.setGeometry(QtCore.QRect(40, 50, 781, 121))
        self.groupBox_4.setStyleSheet("QGroupBox::title {color: rgb(245, 241, 224);}\n"
                                      "QGroupBox {border :2px solid rgb(232, 221, 181);\n"
                                      "                  border-width: 0 0 2px 0;}\n"
                                      "color: rgb(245, 241, 224);")
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit_name = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEdit_name.setGeometry(QtCore.QRect(90, 20, 391, 31))
        self.lineEdit_name.setStyleSheet("border-style: none;\n"
                                         "border-bottom-style: solid;\n"
                                         "border-width: 0 0 2px 0;\n"
                                         "border-color: rgb(71, 115, 154);\n"
                                         "color: white;\n"
                                         "background-color: transparent;")
        self.lineEdit_name.setInputMask("")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setMaxLength(50)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(245, 241, 224);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(700, 20, 81, 31))
        self.pushButton.setStyleSheet("border-radius: 5px;\n"
                                      "color: rgb(245, 241, 224);\n"
                                      "border:2px solid rgb(216, 17, 89);/*rgb(71, 115, 154);2px solid rgb(33, 241, 54);*/")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_id = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEdit_id.setGeometry(QtCore.QRect(530, 20, 51, 31))
        self.lineEdit_id.setStyleSheet("border-style: none;\n"
                                       "border-bottom-style: solid;\n"
                                       "border-width: 0 0 2px 0;\n"
                                       "border-color: rgb(71, 115, 154);\n"
                                       "color: white;\n"
                                       "background-color: transparent;")
        self.lineEdit_id.setInputMask("")
        self.lineEdit_id.setText("")
        self.lineEdit_id.setMaxLength(4)
        self.lineEdit_id.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(500, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(245, 241, 224);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(290, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(245, 241, 224);")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(245, 241, 224);")
        self.label_7.setObjectName("label_7")
        self.GcomboBox = QtWidgets.QComboBox(parent=self.groupBox_4)
        self.GcomboBox.setGeometry(QtCore.QRect(570, 70, 211, 31))
        self.GcomboBox.setStyleSheet("border: 2px solid white;\n"
                                     "border-color:rgb(71, 115, 154);\n"
                                     "color: rgb(245, 241, 224);")
        self.GcomboBox.setObjectName("GcomboBox")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(500, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(245, 241, 224);")
        self.label_6.setObjectName("label_6")
        self.YcomboBox = QtWidgets.QComboBox(parent=self.groupBox_4)
        self.YcomboBox.setGeometry(QtCore.QRect(90, 70, 131, 31))
        self.YcomboBox.setAutoFillBackground(False)
        self.YcomboBox.setStyleSheet("border: 2px solid white;\n"
                                     "border-color:rgb(71, 115, 154);\n"
                                     "color: rgb(245, 241, 224);")
        self.YcomboBox.setCurrentText("")
        self.YcomboBox.setObjectName("YcomboBox")
        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox_4)
        self.comboBox.setGeometry(QtCore.QRect(350, 70, 131, 31))
        self.comboBox.setStyleSheet("border: 2px solid white;\n"
                                    "border-color:rgb(71, 115, 154);\n"
                                    "color: rgb(245, 241, 224);")
        self.comboBox.setObjectName("comboBox")
        self.lineEdit_id_2 = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEdit_id_2.setGeometry(QtCore.QRect(610, 20, 51, 31))
        self.lineEdit_id_2.setStyleSheet("border-style: none;\n"
                                         "border-bottom-style: solid;\n"
                                         "border-width: 0 0 2px 0;\n"
                                         "border-color: rgb(71, 115, 154);\n"
                                         "color: white;\n"
                                         "background-color: transparent;")
        self.lineEdit_id_2.setInputMask("")
        self.lineEdit_id_2.setText("")
        self.lineEdit_id_2.setMaxLength(4)
        self.lineEdit_id_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_id_2.setObjectName("lineEdit_id_2")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(590, 20, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(245, 241, 224);")
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.studentTab, "")
        self.courseTab = QtWidgets.QWidget()
        self.courseTab.setObjectName("courseTab")
        self.courseTable = QtWidgets.QTableView(parent=self.courseTab)
        self.courseTable.setGeometry(QtCore.QRect(40, 150, 781, 531))
        self.courseTable.setStyleSheet(tableStyleSheet)
        self.courseTable.setObjectName("courseTable")
        self.courseTable.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.addCourseLine = QtWidgets.QLineEdit(parent=self.courseTab)
        self.addCourseLine.setGeometry(QtCore.QRect(210, 80, 321, 31))
        self.addCourseLine.setStyleSheet("border-style: none;\n"
                                         "border-bottom-style: solid;\n"
                                         "border-width: 0 0 2px 0;\n"
                                         "border-color: rgb(71, 115, 154);\n"
                                         "color: white;\n"
                                         "background-color: transparent;")
        self.addCourseLine.setInputMask("")
        self.addCourseLine.setText("")
        self.addCourseLine.setObjectName("addCourseLine")
        self.courseLabel = QtWidgets.QLabel(parent=self.courseTab)
        self.courseLabel.setGeometry(QtCore.QRect(210, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.courseLabel.setFont(font)
        self.courseLabel.setStyleSheet("color: rgb(245, 241, 224);")
        self.courseLabel.setObjectName("courseLabel")
        self.addCourseButton = QtWidgets.QPushButton(parent=self.courseTab)
        self.addCourseButton.setGeometry(QtCore.QRect(550, 80, 61, 31))
        self.addCourseButton.setStyleSheet("border-radius: 5px ;\n"
                                           "color: rgb(241, 234, 208);\n"
                                           "border :2px solid rgb(216, 17, 89);")
        self.addCourseButton.setObjectName("addCourseButton")
        self.label = QtWidgets.QLabel(parent=self.courseTab)
        self.label.setGeometry(QtCore.QRect(20, 10, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(245, 241, 224);")
        self.label.setObjectName("label")
        self.editCourseButton = QtWidgets.QPushButton(parent=self.courseTab)
        self.editCourseButton.setGeometry(QtCore.QRect(620, 80, 81, 31))
        self.editCourseButton.setStyleSheet("border-radius: 5px ;\n"
                                            "color: rgb(241, 234, 208);\n"
                                            "border :2px solid rgb(216, 17, 89);")
        self.editCourseButton.setObjectName("editCourseButton")
        self.deleteCourseButton = QtWidgets.QPushButton(parent=self.courseTab)
        self.deleteCourseButton.setGeometry(QtCore.QRect(720, 80, 101, 31))
        self.deleteCourseButton.setStyleSheet("border-radius: 5px ;\n"
                                              "color: rgb(241, 234, 208);\n"
                                              "border :2px solid rgb(216, 17, 89);")
        self.deleteCourseButton.setObjectName("deleteCourseButton")
        self.courseLabel_2 = QtWidgets.QLabel(parent=self.courseTab)
        self.courseLabel_2.setGeometry(QtCore.QRect(40, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.courseLabel_2.setFont(font)
        self.courseLabel_2.setStyleSheet("color: rgb(245, 241, 224);")
        self.courseLabel_2.setObjectName("courseLabel_2")
        self.addCourseLine_2 = QtWidgets.QLineEdit(parent=self.courseTab)
        self.addCourseLine_2.setGeometry(QtCore.QRect(40, 80, 141, 31))
        self.addCourseLine_2.setStyleSheet("border-style: none;\n"
                                           "border-bottom-style: solid;\n"
                                           "border-width: 0 0 2px 0;\n"
                                           "border-color: rgb(71, 115, 154);\n"
                                           "color: white;\n"
                                           "background-color: transparent;")
        self.addCourseLine_2.setInputMask("")
        self.addCourseLine_2.setText("")
        self.addCourseLine_2.setObjectName("addCourseLine_2")
        self.tabWidget.addTab(self.courseTab, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit_name, self.lineEdit_id)
        Dialog.setTabOrder(self.lineEdit_id, self.lineEdit_id_2)
        Dialog.setTabOrder(self.lineEdit_id_2, self.YcomboBox)
        Dialog.setTabOrder(self.YcomboBox, self.comboBox)
        Dialog.setTabOrder(self.comboBox, self.GcomboBox)
        Dialog.setTabOrder(self.GcomboBox, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.lineEdit_name_3)
        Dialog.setTabOrder(self.lineEdit_name_3, self.pushButton_3)
        Dialog.setTabOrder(self.pushButton_3, self.editEntryButton)
        Dialog.setTabOrder(self.editEntryButton, self.deleteStudentButton)
        Dialog.setTabOrder(self.deleteStudentButton, self.studentTable)
        Dialog.setTabOrder(self.studentTable, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.addCourseLine_2)
        Dialog.setTabOrder(self.addCourseLine_2, self.addCourseLine)
        Dialog.setTabOrder(self.addCourseLine, self.addCourseButton)
        Dialog.setTabOrder(self.addCourseButton, self.courseTable)
        Dialog.setTabOrder(self.courseTable, self.editCourseButton)
        Dialog.setTabOrder(self.editCourseButton, self.deleteCourseButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.editEntryButton.setText(_translate("Dialog", "REFRESH"))
        self.deleteStudentButton.setText(_translate("Dialog", "DELETE ENTRY"))
        self.label_9.setText(_translate(
            "Dialog", "Simple Student Information System (SSIS)"))
        self.lineEdit_name_3.setPlaceholderText(
            _translate("Dialog", "Enter Name or ID"))
        self.label_8.setText(_translate("Dialog", "  Search"))
        self.pushButton_3.setText(_translate("Dialog", "SEARCH"))
        self.groupBox_4.setTitle(_translate("Dialog", "Add Student"))
        self.lineEdit_name.setPlaceholderText(
            _translate("Dialog", "Enter name..."))
        self.label_2.setText(_translate("Dialog", "   Name"))
        self.pushButton.setText(_translate("Dialog", "ADD"))
        self.lineEdit_id.setPlaceholderText(_translate("Dialog", "Enter..."))
        self.label_4.setText(_translate("Dialog", "ID"))
        self.label_5.setText(_translate("Dialog", "Course"))
        self.label_7.setText(_translate("Dialog", "    Year"))
        self.label_6.setText(_translate("Dialog", "Gender"))
        self.lineEdit_id_2.setPlaceholderText(_translate("Dialog", "Enter..."))
        self.label_10.setText(_translate("Dialog", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.studentTab), _translate("Dialog", "Student"))
        self.addCourseLine.setPlaceholderText(_translate("Dialog", "Course"))
        self.courseLabel.setText(_translate("Dialog", "Course"))
        self.addCourseButton.setText(_translate("Dialog", "ADD"))
        self.label.setText(_translate(
            "Dialog", "Simple Student Information System (SSIS)"))
        self.editCourseButton.setText(_translate("Dialog", "REFRESH"))
        self.deleteCourseButton.setText(_translate("Dialog", "DELETE ENTRY"))
        self.courseLabel_2.setText(_translate("Dialog", "Course Code"))
        self.addCourseLine_2.setPlaceholderText(
            _translate("Dialog", "Course Code"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.courseTab), _translate("Dialog", "Course"))
