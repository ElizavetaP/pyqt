import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication,
    QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Communicate(QObject):

    updateBW = pyqtSignal()


class BurningWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setMinimumSize(600, 600)
        self.value = 0
        


    def setValue(self):

        self.value = 1


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()


    def drawWidget(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(QColor('White'))
        qp.drawRect(0, 0, 600, 600)


        if self.value == 1:
            qp.setBrush(QColor('Blue'))
            #qp.setPen(QPen(QBrush(Qt.blue), 2, Qt.SolidLine))
            self.polygon = QPolygon([QPoint(100, 130), QPoint(300, 130),QPoint(200, 20),QPoint(100, 130)])
            
            qp.drawPolygon(self.polygon)


       
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

       

        self.c = Communicate()
        self.wid = BurningWidget()
        self.c.updateBW.connect(self.wid.setValue)

        #sld.valueChanged[int].connect(self.changeValue)
        hbox = QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Burning widget')
        self.show()


    def mousePressEvent(self, event):

        self.c.updateBW.emit()
        self.wid.repaint()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
