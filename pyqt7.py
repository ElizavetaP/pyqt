import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
from datetime import datetime, timedelta, date, time as dt_time


class Communicate(QObject):

    updateBW = pyqtSignal()


class BurningWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setMinimumSize(1200, 800)
        self.value = 0
        
    def setValue(self):

        self.value = self.value + 1
        
    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()


    def drawWidget(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        if self.value <= 1:
            qp.setBrush(QColor('Blue'))
            qp.drawRect(0, 0, 1200, 800)

        if self.value == 1:
            qp.setBrush(QColor('Yellow'))
            self.polygon = QPolygon([QPoint(450, 530), QPoint(750, 530),QPoint(600, 270),QPoint(450, 530)])
            
            qp.drawPolygon(self.polygon)
            
        if self.value > 1:
            qp.setBrush(QColor('White'))
            qp.drawRect(0, 0, 1200, 800)
       
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.c = Communicate()
        self.wid = BurningWidget()
        self.c.updateBW.connect(self.wid.setValue)
        
        le = QLineEdit(self)
        le.move(130, 22)
        text, ok = QInputDialog.getText(self, 'Input Dialog',
        'Enter your name:')

        if ok:
            le.setText(str(text))
            self.file = open("""/home/an/%(data)s.txt"""%{'data':text}, 'a')
            print (text)
            
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(300, 150, 1200, 800)
        self.setWindowTitle('Burning widget')
        self.show()

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Tab:

            self.c.updateBW.emit()
            self.wid.repaint()
            t = time.time()
            j = 0
            while j<=7:
                j = time.time() - t
            print (j)
            self.c.updateBW.emit()
            self.wid.repaint()
            
        if e.key() == Qt.Key_F1:
            self.c.updateBW.emit()
            self.wid.repaint()
            self.CurrentTime = time.time()
            print(self.CurrentTime)

        if e.key() == Qt.Key_F2:
            self.CurrentTime =  time.time() - self.CurrentTime
            print(self.CurrentTime)
            d = datetime.today()
            self.file.write(str(d.date()))
            self.file.write('\n')
            self.file.write(str(round(self.CurrentTime,1)))
            self.file.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
