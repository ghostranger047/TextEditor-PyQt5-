from PyQt5 import QtWidgets, QtCore, QtGui
from font import Ui_FontWindow
import sys

class ControlFont(QtWidgets.QMainWindow, Ui_FontWindow):
    classEdit = None
    def __init__(self, edit):
        super(ControlFont, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.setFont)
        for i in range(2, 51):
            self.fontSize.addItem(str(i))
        self.classEdit = edit
        self.label_3.setText('Font color:')
        


    def setFont(self):
        #print(int(self.fontSize))
        bol = False
        if self.checkBold.isChecked():
            bol = True
          
        font = QtGui.QFont()
        font.setPointSize(int(str(self.fontSize.currentText())))
        font.setFamily(self.fontComboBox.currentText())
        font.setBold(bol)
        self.classEdit.setStyleSheet("color: rgb("+str(self.fontColor.toPlainText())+")")
        self.classEdit.setFont(font)