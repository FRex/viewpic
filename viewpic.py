import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QFrame
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt


class MyPicLabel(QLabel):
    def __init__(self, pixmap):
        super(MyPicLabel, self).__init__()
        self.pixmap = pixmap
        self.setMinimumSize(32, 32)
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        if self.pixmap:
            self.setPixmap(self.pixmap)

    def resizeEvent(self, event):
        if self.pixmap:
            self.setPixmap(self.pixmap.scaled(event.size(), Qt.AspectRatioMode.KeepAspectRatio))


class MyMainWindow(QMainWindow):
    def __init__(self, picpath):
        super(MyMainWindow, self).__init__()
        self.setWindowTitle(picpath)
        self.setAcceptDrops(True)
        p = MyPicLabel(QPixmap(picpath))
        p.setFrameShape(QFrame.Shape.Box)
        self.setCentralWidget(p)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        print(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow(sys.argv[1])
    win.show()
    sys.exit(app.exec_())
