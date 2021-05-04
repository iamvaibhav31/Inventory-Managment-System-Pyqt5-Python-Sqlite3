# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainBmRWWS.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(782, 706)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 80, 761, 441))
        self.tabWidget.setStyleSheet(u"font: italic 16pt \"Century Gothic\";")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 581, 41))
        self.label_2.setMinimumSize(QSize(0, 8))
        self.table = QTableWidget(self.tab)
        if (self.table.columnCount() < 9):
            self.table.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(5, 110, 741, 281))
        self.table.setStyleSheet(u"font: italic 9pt \"Century Gothic\";")
        self.search_btn = QPushButton(self.tab)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(600, 50, 141, 51))
        self.count_filter_txt = QLineEdit(self.tab)
        self.count_filter_txt.setObjectName(u"count_filter_txt")
        self.count_filter_txt.setGeometry(QRect(600, 19, 141, 31))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 20, 221, 31))
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 70, 241, 31))
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 20, 241, 31))
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(320, 70, 241, 31))
        self.lbl_ref_nbr = QLabel(self.tab_2)
        self.lbl_ref_nbr.setObjectName(u"lbl_ref_nbr")
        self.lbl_ref_nbr.setGeometry(QRect(250, 30, 21, 21))
        self.lbl_ref_nbr.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.lbl_ref_nbr.setAlignment(Qt.AlignCenter)
        self.lbl_part_nbr = QLabel(self.tab_2)
        self.lbl_part_nbr.setObjectName(u"lbl_part_nbr")
        self.lbl_part_nbr.setGeometry(QRect(260, 70, 21, 31))
        self.lbl_part_nbr.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.lbl_part_nbr.setAlignment(Qt.AlignCenter)
        self.lbl_min_hole = QLabel(self.tab_2)
        self.lbl_min_hole.setObjectName(u"lbl_min_hole")
        self.lbl_min_hole.setGeometry(QRect(560, 20, 21, 31))
        self.lbl_min_hole.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.lbl_min_hole.setAlignment(Qt.AlignCenter)
        self.lbl_max_holes = QLabel(self.tab_2)
        self.lbl_max_holes.setObjectName(u"lbl_max_holes")
        self.lbl_max_holes.setGeometry(QRect(560, 70, 21, 31))
        self.lbl_max_holes.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.lbl_max_holes.setAlignment(Qt.AlignCenter)
        self.table2 = QTableWidget(self.tab_2)
        if (self.table2.columnCount() < 3):
            self.table2.setColumnCount(3)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        self.table2.setObjectName(u"table2")
        self.table2.setGeometry(QRect(10, 200, 531, 192))
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 140, 711, 51))
        self.label_6.setAlignment(Qt.AlignCenter)
        self.check_btn = QPushButton(self.tab_2)
        self.check_btn.setObjectName(u"check_btn")
        self.check_btn.setGeometry(QRect(560, 200, 181, 191))
        self.check_btn.setStyleSheet(u"QPushButton\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #4A4949;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 4px;\n"
"    /* outline: none; */\n"
"    /* min-width: 40px; */\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #808080;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #3d8ec9;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #4A4949;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"")
        self.lbl_min_hole_2 = QLabel(self.tab_2)
        self.lbl_min_hole_2.setObjectName(u"lbl_min_hole_2")
        self.lbl_min_hole_2.setGeometry(QRect(650, 30, 51, 21))
        self.lbl_min_hole_2.setAlignment(Qt.AlignCenter)
        self.lbl_max_holes_2 = QLabel(self.tab_2)
        self.lbl_max_holes_2.setObjectName(u"lbl_max_holes_2")
        self.lbl_max_holes_2.setGeometry(QRect(650, 80, 51, 21))
        self.lbl_max_holes_2.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 100, 111, 21))
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 130, 111, 21))
        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 160, 101, 21))
        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(400, 160, 151, 21))
        self.label_12 = QLabel(self.tab_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(400, 130, 151, 21))
        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(400, 100, 171, 21))
        self.label_14 = QLabel(self.tab_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(30, 190, 101, 21))
        self.label_15 = QLabel(self.tab_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(440, 190, 71, 21))
        self.label_16 = QLabel(self.tab_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(250, 30, 41, 31))
        self.reference = QLineEdit(self.tab_3)
        self.reference.setObjectName(u"reference")
        self.reference.setGeometry(QRect(160, 100, 113, 20))
        self.reference.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.part_name = QLineEdit(self.tab_3)
        self.part_name.setObjectName(u"part_name")
        self.part_name.setGeometry(QRect(160, 130, 113, 20))
        self.part_name.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.min_area = QLineEdit(self.tab_3)
        self.min_area.setObjectName(u"min_area")
        self.min_area.setGeometry(QRect(160, 160, 113, 20))
        self.min_area.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.max_area = QLineEdit(self.tab_3)
        self.max_area.setObjectName(u"max_area")
        self.max_area.setGeometry(QRect(160, 190, 113, 20))
        self.max_area.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.number_of_holes = QLineEdit(self.tab_3)
        self.number_of_holes.setObjectName(u"number_of_holes")
        self.number_of_holes.setGeometry(QRect(590, 100, 113, 20))
        self.number_of_holes.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.min_diameter = QLineEdit(self.tab_3)
        self.min_diameter.setObjectName(u"min_diameter")
        self.min_diameter.setGeometry(QRect(590, 130, 113, 20))
        self.min_diameter.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.max_diameter = QLineEdit(self.tab_3)
        self.max_diameter.setObjectName(u"max_diameter")
        self.max_diameter.setGeometry(QRect(590, 160, 113, 20))
        self.max_diameter.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.next_btn = QPushButton(self.tab_3)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setGeometry(QRect(180, 270, 71, 41))
        self.last_btn = QPushButton(self.tab_3)
        self.last_btn.setObjectName(u"last_btn")
        self.last_btn.setGeometry(QRect(260, 270, 71, 41))
        self.previous_btn = QPushButton(self.tab_3)
        self.previous_btn.setObjectName(u"previous_btn")
        self.previous_btn.setGeometry(QRect(100, 270, 71, 41))
        self.first_btn = QPushButton(self.tab_3)
        self.first_btn.setObjectName(u"first_btn")
        self.first_btn.setGeometry(QRect(20, 270, 71, 41))
        self.update_btn = QPushButton(self.tab_3)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setGeometry(QRect(520, 20, 101, 41))
        self.delete_btn = QPushButton(self.tab_3)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setGeometry(QRect(590, 270, 141, 41))
        self.add_btn = QPushButton(self.tab_3)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(460, 270, 121, 41))
        self.count = QLineEdit(self.tab_3)
        self.count.setObjectName(u"count")
        self.count.setGeometry(QRect(590, 190, 113, 20))
        self.count.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.enter_btn = QPushButton(self.tab_3)
        self.enter_btn.setObjectName(u"enter_btn")
        self.enter_btn.setGeometry(QRect(410, 20, 101, 41))
        self.id = QLineEdit(self.tab_3)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(300, 30, 71, 31))
        self.id.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.tabWidget.addTab(self.tab_3, "")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 761, 51))
        self.label.setStyleSheet(u"font: italic 26pt \"Century Gothic\";\n"
"color: rgb(176, 107, 255);\n"
"background-color: rgb(193, 193, 193);")
        self.label.setAlignment(Qt.AlignCenter)
        self.refresh_btn = QPushButton(self.centralwidget)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.setGeometry(QRect(610, 540, 151, 71))
        self.refresh_btn.setStyleSheet(u"font: italic 16pt \"Century Gothic\";QPushButton\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #4A4949;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 4px;\n"
"    /* outline: none; */\n"
"    /* min-width: 40px; */\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #808080;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #3d8ec9;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #4A4949;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #78879b;\n"
"    color: silv"
                        "er;\n"
"}\n"
"")
        self.error = QLabel(self.centralwidget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(10, 640, 761, 21))
        self.error.setFrameShape(QFrame.StyledPanel)
        self.error.setAlignment(Qt.AlignCenter)
        self.error.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 782, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"part inventory manager", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"search of referance with count level lower of equal to :-", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Referance", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"part name", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"min area", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"max area", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Nbr of holes", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"min diameter", None));
        ___qtablewidgetitem7 = self.table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"max diameter", None));
        ___qtablewidgetitem8 = self.table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"count", None));
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Inventory Details", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Number of referece :-", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Number of part type :-", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"min Number of holes :-", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"max Number of holes :-", None))
        self.lbl_ref_nbr.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_part_nbr.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_min_hole.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_max_holes.setText(QCoreApplication.translate("MainWindow", u"0", None))
        ___qtablewidgetitem9 = self.table2.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Reference", None));
        ___qtablewidgetitem10 = self.table2.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Part name", None));
        ___qtablewidgetitem11 = self.table2.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"count", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Top 3 reference with minimum iventory level", None))
        self.check_btn.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.lbl_min_hole_2.setText(QCoreApplication.translate("MainWindow", u"REF", None))
        self.lbl_max_holes_2.setText(QCoreApplication.translate("MainWindow", u"REF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Inventory statistics", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Reference", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Part name", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Min Area", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Max Diameter", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"MIn Diameter", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Number of Holes", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Max Area", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Count", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"ID :-", None))
        self.reference.setInputMask("")
        self.reference.setText("")
        self.part_name.setInputMask("")
        self.part_name.setText("")
        self.min_area.setInputMask("")
        self.min_area.setText("")
        self.max_area.setInputMask("")
        self.max_area.setText("")
        self.number_of_holes.setInputMask("")
        self.number_of_holes.setText("")
        self.min_diameter.setInputMask("")
        self.min_diameter.setText("")
        self.max_diameter.setInputMask("")
        self.max_diameter.setText("")
        self.next_btn.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.last_btn.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.previous_btn.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.first_btn.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete Item's", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Add Item's", None))
        self.count.setInputMask("")
        self.count.setText("")
        self.enter_btn.setText(QCoreApplication.translate("MainWindow", u"ENTER", None))
        self.id.setInputMask("")
        self.id.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Edit invertory", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Part inventory manager", None))
        self.refresh_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.error.setText("")
    # retranslateUi

