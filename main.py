from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow , QApplication ,QTableWidgetItem
import sys
from os import path
from PyQt5.uic import loadUiType
import sqlite3
from qtmodern.styles import dark
from qtmodern.windows import ModernWindow


FROM_CLASS,_=loadUiType(path.join(path.dirname("__file__"),"main.ui"))


class Main(QMainWindow , FROM_CLASS):
    
    def __init__(self , parent = None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.id.setPlaceholderText("ID")
        self.reference.setPlaceholderText("REFERENCE")
        self.part_name.setPlaceholderText("PART NAME")
        self.min_area.setPlaceholderText("MIN AREA")
        self.max_area.setPlaceholderText("MAX AREA")
        self.number_of_holes.setPlaceholderText("NO. OF HOLES")
        self.min_diameter.setPlaceholderText("MIN DIAMETER")
        self.max_diameter.setPlaceholderText("MAX DIAMETER")
        self.count.setPlaceholderText("COUNT")
        self.Handel_button()
        self.no_of_time_button_press = 0
        self.data_base = sqlite3.connect("part.db")
        self.cursor = self.data_base.cursor()

    def Handel_button(self):
        self.refresh_btn.clicked.connect(self.GET_DATA)
        self.search_btn.clicked.connect(self.search)
        self.count_filter_txt.returnPressed.connect(self.search)
        self.check_btn.clicked.connect(self.check)
        self.id.returnPressed.connect(self.enter)
        self.enter_btn.clicked.connect(self.enter)
        self.update_btn.clicked.connect(self.update)
        self.add_btn.clicked.connect(self.add)
        self.delete_btn.clicked.connect(self.delete)
        self.next_btn.clicked.connect(self.next)
        self.previous_btn.clicked.connect(self.previous)
        self.last_btn.clicked.connect(self.last)
        self.first_btn.clicked.connect(self.first)

    
    def GET_DATA(self):
        command = """ SELECT * from parts_table """
        result = self.cursor.execute(command)
        self.table.setRowCount(0)
        for row_count , row_data in enumerate(result):
            self.table.insertRow(row_count)
            for column_number , data in enumerate(row_data):
                self.table.setItem(row_count , column_number , QTableWidgetItem(str(data)))
        
        cursor2 = self.data_base.cursor()
        cursor3 = self.data_base.cursor()
        refs= """SELECT COUNT (DISTINCT reference) from parts_table"""
        result_ref = cursor2.execute(refs)
        parts = """ SELECT COUNT (DISTINCT partname) from parts_table"""
        result_parts  = cursor3.execute(parts)
        self.lbl_ref_nbr.setText(str(result_ref.fetchone()[0]))
        self.lbl_part_nbr.setText(str(result_parts.fetchone()[0]))

        cursor4 = self.data_base.cursor()
        curson5 = self.data_base.cursor()
        min_hole = ''' SELECT  min(numberofholes), reference from parts_table'''
        max_hole = ''' SELECT  max(numberofholes), reference from parts_table'''
        result_minh = cursor4.execute(min_hole)
        result_maxh = curson5.execute(max_hole)
        r1 = result_minh.fetchone()
        r2 = result_maxh.fetchone()
        self.lbl_min_hole.setText(str(r1[0]))
        self.lbl_max_holes.setText(str(r2[0]))
        self.lbl_min_hole_2.setText(str(r1[1]))
        self.lbl_max_holes_2.setText(str(r2[1]))
    
    def search(self):
        nbr = int(self.count_filter_txt.text())
        command = """ SELECT * from parts_table WHERE count<=?"""
        result = self.cursor.execute(command,[nbr])
        self.table.setRowCount(0)
        for row_count , row_data in enumerate(result):
            self.table.insertRow(row_count)
            for column_number , data in enumerate(row_data):
                self.table.setItem(row_count , column_number , QTableWidgetItem(str(data)))

    def check(self):
        command = """ SELECT reference , partname , count from parts_table order by count asc LIMIT 3 """
        result = self.cursor.execute(command)
        self.table2.setRowCount(0)
        for row_count , row_data in enumerate(result):
            self.table2.insertRow(row_count)
            for column_number , data in enumerate(row_data):
                self.table2.setItem(row_count , column_number , QTableWidgetItem(str(data)))

    def enter(self):
        id_ = self.id.text()
        command  =  """ SELECT * from parts_table WHERE id=? """
        result = self.cursor.execute(command , [id_])
        val  = result.fetchone()

        self.reference.setText(str(val[1]))
        self.part_name.setText(str(val[2]))
        self.min_area.setText(str(val[3]))
        self.max_area.setText(str(val[4]))
        self.number_of_holes.setText(str(val[5]))
        self.min_diameter.setText(str(val[6]))
        self.max_diameter.setText(str(val[7]))
        self.count.setText(str(val[8]))

    def update(self):
        id_ = self.id.text()
        reference_=self.reference.text()
        partname_=self.part_name.text()
        minarea_= self.min_area.text()
        maxarea_=self.max_area.text()
        numberofholes_= self.number_of_holes.text()
        mindiameter_=self.min_diameter.text()
        maxdiameter_=self.max_diameter.text()
        count_=self.count.text()
        update_row = (reference_,partname_,minarea_,maxarea_,numberofholes_,mindiameter_,maxdiameter_,count_,id_)
        command  = """UPDATE parts_table SET reference = ? , partname = ? , minarea = ? , maxarea = ? , numberofholes = ? , mindiameter = ? , maxdiameter = ? , count = ? WHERE id = ? """
        self.cursor.execute(command , update_row)
        self.data_base.commit()
    
    def delete(self):
        id_=self.id.text()
        command = """ DELETE FROM parts_table WHERE id = ? """
        self.cursor.execute(command,[id_])
        self.data_base.commit()
    
    def add(self):
        id_ = self.id.text()
        reference_=self.reference.text()
        partname_=self.part_name.text()
        minarea_= self.min_area.text()
        maxarea_=self.max_area.text()
        numberofholes_= self.number_of_holes.text()
        mindiameter_=self.min_diameter.text()
        maxdiameter_=self.max_diameter.text()
        count_=self.count.text()
        update_row = (id_,reference_,partname_,minarea_,maxarea_,numberofholes_,mindiameter_,maxdiameter_,count_)
        command  = """INSERT INTO parts_table (id,reference, partname, minarea, maxarea, numberofholes, mindiameter, maxdiameter, count) VALUES(?,?,?,?,?,?,?,?,?) """
        self.cursor.execute(command , update_row)
        self.data_base.commit()
    
    def first(self):
        command="""SELECT * FROM parts_table"""
        result = self.cursor.execute(command)
        r1 = result.fetchall()
        self.id.setText(str(r1[0][0]))
        self.reference.setText(str(r1[0][1]))
        self.part_name.setText(str(r1[0][2]))
        self.min_area.setText(str(r1[0][3]))
        self.max_area.setText(str(r1[0][4]))
        self.number_of_holes.setText(str(r1[0][5]))
        self.min_diameter.setText(str(r1[0][6]))
        self.max_diameter.setText(str(r1[0][7]))
        self.count.setText(str(r1[0][8]))
    
    def last(self):
        command="""SELECT * FROM parts_table"""
        result = self.cursor.execute(command)
        r1 = result.fetchall()
        self.id.setText(str(r1[-1][0]))
        self.reference.setText(str(r1[-1][1]))
        self.part_name.setText(str(r1[-1][2]))
        self.min_area.setText(str(r1[-1][3]))
        self.max_area.setText(str(r1[-1][4]))
        self.number_of_holes.setText(str(r1[-1][5]))
        self.min_diameter.setText(str(r1[-1][6]))
        self.max_diameter.setText(str(r1[-1][7]))
        self.count.setText(str(r1[-1][8]))

    def next(self):
        command="""SELECT * FROM parts_table"""
        result = self.cursor.execute(command)
        r1 = result.fetchall()
        self.no_of_time_button_press +=1
        if self.no_of_time_button_press > 0 and self.no_of_time_button_press < len(r1)-1:
            self.print(self.no_of_time_button_press)
    
    def previous(self):
        command="""SELECT * FROM parts_table"""
        result = self.cursor.execute(command)
        r1 = result.fetchall()
        self.no_of_time_button_press -=1
        if self.no_of_time_button_press > 0 and self.no_of_time_button_press < len(r1)-1:
            self.print(self.no_of_time_button_press)

    
    def print(self , temp):
        command="""SELECT * FROM parts_table"""
        result = self.cursor.execute(command)
        r1 = result.fetchall()
        self.id.setText(str(r1[temp][0]))
        self.reference.setText(str(r1[temp][1]))
        self.part_name.setText(str(r1[temp][2]))
        self.min_area.setText(str(r1[temp][3]))
        self.max_area.setText(str(r1[temp][4]))
        self.number_of_holes.setText(str(r1[temp][5]))
        self.min_diameter.setText(str(r1[temp][6]))
        self.max_diameter.setText(str(r1[temp][7]))
        self.count.setText(str(r1[temp][8]))

def main():

    app = QApplication(sys.argv) 
    window = Main()
    window.GET_DATA()
    window.check()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()    