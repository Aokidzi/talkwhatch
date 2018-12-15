import   design.calculator as calculator
import sys
from  PyQt5 import QtWidgets
import os

class ExamoleAPP(QtWidgets.QMainWindow, calculator.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textView=''
        self.x1=''
        self.action=''
        self.BUTTONFIVE.clicked.connect(self.click1)
        self.BUTTONSEVEN.clicked.connect(self.click0)
        self.BUTTONTWO.clicked.connect(self.click2)
        self.BUTTONDELIT.clicked.connect(self.click3)
        self.BUTTONFOUR.clicked.connect(self.click4)
        self.BUTTONONE.clicked.connect(self.click5)
        self.BUTTONUMNOJIT.clicked.connect(self.click6)
        self.pushButton_8.clicked.connect(self.click7)
        self.pushButton_7.clicked.connect(self.click8)
        self.BUTTONZAPYATAYA.clicked.connect(self.click9)
        self.BUTTONAC.clicked.connect(self.clickAC)
        self.BUTTONTREE.clicked.connect(self.clickTREE)
        self.BUTTONZERO.clicked.connect(self.clickZERO)
        self.BUTTONNINE.clicked.connect(self.clickNINE)
        self.BUTTONPLUS.clicked.connect(self.clickPLUS)
        self.pushButton_9.clicked.connect(self.click_9)
        self.BUTTONMINUC.clicked.connect(self.clickMINUC)


    def clickNINE(self):
        self.textView=self.textView[:-1]
        self.OTVET.setText(self.textView)


    def clickMINUC(self):
        if self.action=='+':
            self.textView=str(float(self.x1)+float(self.textView))
        elif self.action=='-':
            self.textView=str(float(self.x1)-float(self.textView))
        elif self.action=='*':
            self.textView=str(float(self.x1)*float(self.textView))
        elif self.action=='/':
            self.textView=str(float(self.x1)/float(self.textView))
        self.OTVET.setText(self.textView)


    def click_9(self):
        self.action='-'
        self.x1=self.textView
        self.textView=''
        self.OTVET.setText(self.textView)


    def clickPLUS(self):
        self.action='+'
        self.x1=self.textView
        self.textView=''
        self.textView=self.textView[:-1]
        self.OTVET.setText(self.textView)


    def clickZERO(self):
        if not self.textView=='' :
            if not '-' in self.textView:
                self.textView = '-'+self.textView
                self.OTVET.setText(self.textView)
            else:
                self.textView = self.textView[1:]
                self.OTVET.setText(self.textView)


    def clickAC(self):
        self.textView=''
        self.OTVET.setText(self.textView)

    def clickTREE(self):
        if not self.textView=='':
            if not '.' in self.textView:
                self.textView+='.'
                self.OTVET.setText(self.textView)

    def click1(self):
        self.textView+='1'
        self.OTVET.setText(self.textView)

    def click0(self):
        self.textView+='0'
        self.OTVET.setText(self.textView)

    def click2(self):
        self.textView+='2'
        self.OTVET.setText(self.textView)

    def click3(self):
        self.textView+='3'
        self.OTVET.setText(self.textView)

    def click4(self):
        self.textView+='4'
        self.OTVET.setText(self.textView)

    def click5(self):
        self.textView += '5'
        self.OTVET.setText(self.textView)

    def click6(self):
        self.textView += '6'
        self.OTVET.setText(self.textView)

    def click7(self):
        self.textView += '7'
        self.OTVET.setText(self.textView)

    def click8(self):
        self.textView += '8'
        self.OTVET.setText(self.textView)

    def click9(self):
        self.textView += '9'
        self.OTVET.setText(self.textView)





app = QtWidgets.QApplication(sys.argv)
window = ExamoleAPP()
window.show()
app.exec()