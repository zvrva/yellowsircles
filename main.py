import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import choice


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.circles)
        self.go = True

    def circles(self):
        self.go = True

    def paintEvent(self, event):
        if self.go:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
            # self.go = False

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        c = []
        for i in range(0, 300):
            c.append(i)
        f = choice([1, 2, 3, 4])
        for i in range(f):
            a = choice(c)
            b = choice(c)
            d = choice(c)
            print(a, b, d)
            qp.drawEllipse(a, b, a + d, b + d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
