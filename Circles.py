import sys
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from random import randint
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('shar.ui', self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.click.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.run(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def run(self, qp):
        qp.setBrush(QColor('yellow'))
        a = randint(20, 100)
        x = randint(50, 650)
        y = randint(50, 300)
        qp.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
