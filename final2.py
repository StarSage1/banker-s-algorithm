# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
#i
from final3 import Ui_window3
class Ui_window2(object):
    def setupUi(self, window2):
        window2.setObjectName("window2")
        window2.resize(654, 210)
        self.centralwidget = QtWidgets.QWidget(window2)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(180, 40, 461, 91))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(1)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 150, 151, 41))
        self.pushButton.clicked.connect(self.readdata)
        self.pushButton.setObjectName("pushButton")
        window2.setCentralWidget(self.centralwidget)

        self.retranslateUi(window2)
        QtCore.QMetaObject.connectSlotsByName(window2)

    def retranslateUi(self, window2):
        _translate = QtCore.QCoreApplication.translate
        window2.setWindowTitle(_translate("window2", "MainWindow"))
        self.label.setText(_translate("window2", "Maximum resources"))
        self.pushButton.setText(_translate("window2", "next"))



    #get data number of resources from window1
    def getdata(self,data):
        self.data = data
        self.getdata=self.data

    #read data from the table and store it in a list
    def readdata(self):
        self.maxres=[]
        for i in range(self.tableWidget.columnCount()):
            self.maxres.append(int(self.tableWidget.item(0,i).text()))
        #make it to window3
        print(self.maxres)
        self.window3=QtWidgets.QMainWindow()
        self.ui=Ui_window3()
        self.ui.setupUi(self.window3)
        self.window3.show()
        self.centralwidget.window().hide()
        #count the number of values in the self.maxres[]
        self.count=len(self.maxres)

        #settign values for table1
        #send the value to be the number of rows in tablewidget in final3
        self.ui.tableWidget.setColumnCount(self.count)
        self.ui.tableWidget.setHorizontalHeaderLabels([f"R{i+1}" for i in range(self.count)])
        self.ui.tableWidget.setRowCount(int(self.getdata))
        # self.ui.tableWidget.setHorizontalHeaderLabels([f"R{i+1}" for i in range(int(self.resources))])
        self.ui.tableWidget.setVerticalHeaderLabels([f"P{i+1}" for i in range(int(self.getdata))])
        
        #setting vaues to table2
        self.ui.tableWidget_2.setColumnCount(self.count)
        self.ui.tableWidget_2.setHorizontalHeaderLabels([f"R{i+1}" for i in range(self.count)])
        self.ui.tableWidget_2.setRowCount(int(self.getdata))
        # self.ui.tableWidget.setHorizontalHeaderLabels([f"R{i+1}" for i in range(int(self.resources))])
        self.ui.tableWidget_2.setVerticalHeaderLabels([f"P{i+1}" for i in range(int(self.getdata))])
        #send maxres[] to get_list in window3
        self.ui.getdata(self.maxres)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window2 = QtWidgets.QMainWindow()
    ui = Ui_window2()
    ui.setupUi(window2)
    window2.show()
    sys.exit(app.exec_())