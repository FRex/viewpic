import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QFrame
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt, QUrl


class MyPicLabel(QLabel):
    def __init__(self):
        super(MyPicLabel, self).__init__()
        self.pixmap = None
        self.setMinimumSize(32, 32)
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

    def setPixmap(self, pixmap):
        oldpixmap = self.pixmap
        self.pixmap = pixmap
        if oldpixmap is None or self.pixmap.isNull():
            super(MyPicLabel, self).setPixmap(self.pixmap)
        elif not self.pixmap.isNull():
            scaled = self.pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            super(MyPicLabel, self).setPixmap(scaled)

    def resizeEvent(self, event):
        if self.pixmap and not self.pixmap.isNull():
            scaled = self.pixmap.scaled(event.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            super(MyPicLabel, self).setPixmap(scaled)


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.label = MyPicLabel()
        self.setAcceptDrops(True)
        self.setMinimumSize(256, 128)
        self.setCentralWidget(self.label)

    def openPicture(self, fname):
        self.setWindowTitle(fname)
        p = QPixmap(fname)
        self.label.setPixmap(p)
        return not p.isNull()

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        md = event.mimeData()
        if md.hasUrls() and len(md.urls()) >= 1:
            url = md.urls()[0].url()
            if url.startswith('file:///'):
                url = url[len('file:///'):]
            if self.openPicture(url):
                event.acceptProposedAction()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    if len(sys.argv) > 1:
        win.openPicture(sys.argv[1])
    win.show()
    sys.exit(app.exec_())
