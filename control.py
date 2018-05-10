from PyQt5 import QtWidgets, QtCore, QtGui
from TextEditor import Ui_MainWindow
from Controlfont import ControlFont
import sys

class Control(QtWidgets.QMainWindow, Ui_MainWindow):
    edit = None
    saveloc = ""
    def __init__(self):
        super(Control, self).__init__()
        self.setupUi(self)
        self.actionEditFonts.triggered.connect(self.fontWindow)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave_as.triggered.connect(self.saveFile)
        self.actionSave.triggered.connect(self.save)
        self.actionExit.triggered.connect(self.exitProg)
        self.edit = self.plainTextEdit


    def openFile(self):
        options = QtWidgets.QFileDialog.Options()
        loc, _ = QtWidgets.QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        with open(loc , 'r') as f:
            lines = f.readlines()
        for str in lines:
            self.plainTextEdit.appendPlainText(str[:-2])



    def saveFile(self):
        options = QtWidgets.QFileDialog.Options()
        loc, _ = QtWidgets.QFileDialog.getSaveFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        self.saveloc = loc
        lines = self.plainTextEdit.toPlainText()
        with open(loc, 'w') as data:
            for str in lines:
                data.write(str)
        data.close()


    def save(self):
        #print(self.saveloc)
        if self.saveloc == "":
            self.saveFile()
        else:
            lines = self.plainTextEdit.toPlainText()
            with open(self.saveloc, 'w') as data:
                for str in lines:
                    data.write(str)
            data.close()


    def fontWindow(self):
        self.openFont = ControlFont(self.plainTextEdit)
        self.openFont.show()


    def exitProg(self):
        exit() 



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = Control()
    form.show()
    sys.exit(app.exec_())