import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit,
    QInputDialog, QApplication, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
from datetime import datetime

class Communicate(QObject):

    updateBW = pyqtSignal()

    
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI0()
        self.updateUi()
        self.setGeometry(100, 100, 1000, 800)
        self.col = QColor(97,97,97,160)
        self.setStyleSheet("QWidget { background-color: %s }" %
            self.col.name())

        self.show()
    def initUI0(self):

        self.f = open('names.txt')
        self.lines = [line.rstrip('\n') for line in self.f]
        self.j =0

        
        self.i = 1
        self.c = Communicate()
        self.c.updateBW.connect(self.updateUi)
        self.lbl = QLabel(self)

        
        le = QLineEdit(self)
        le.move(130, 22)
        text, ok = QInputDialog.getText(self, 'Input Dialog',
        'Enter your name:')

        if ok:
            le.setText(str(text))
            self.myfile = """/home/an/pyqt/%(data)s.txt"""%{'data':text}
            self.file = open(self.myfile, 'a')
            self.file.write('\n')
            d = datetime.today()
            self.file.write(str(d.strftime('%y-%m-%d %H:%M:%S')))
            self.file.write('\n')
            le.close()
        
        
    def updateUi(self):
        
        if self.i > 0:
            if self.j < len(self.lines):
                self.t0 = time.time()
                self.lbl.setPixmap(QPixmap("""%(name)s.png"""%{'name':str(self.lines[self.j])}).scaled(1000, 700, Qt.KeepAspectRatio))
                self.j = self.j + 1
                if self.j == len(self.lines)-1:
                    print('on')
                    self.f.close()
                    self.f1 = open('/home/an/pyqt/11/names1.txt')
                    self.lines1 = [line.rstrip('\n') for line in self.f1]
                    self.g =0
            else:
                if self.g < len(self.lines):
                    self.t0 = time.time()
                    self.lbl.setPixmap(QPixmap("""%(name)s.png"""%{'name':str(self.lines1[self.g])}).scaled(1000, 700, Qt.KeepAspectRatio))
                    self.g = self.g + 1
            
        else:
            
            self.lbl.setPixmap(QPixmap("mult_4.png").scaled(1000, 700, Qt.KeepAspectRatio))

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Tab:
            if self.i < 0:
                self.file = open(self.myfile, 'a')
                self.file.write(self.lines[self.j-1] +":  " + str(round(time.time() - self.t0,1)))
                self.file.write('\n')
                self.file.close()
            self.i = self.i*(-1)
            
            self.c.updateBW.emit()
            self.lbl.update()

        if e.key() == Qt.Key_Escape:
            self.f1.close()
            self.close()
            

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
