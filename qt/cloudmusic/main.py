import sys

# from PyQt6.QtWidgets import QApplication, QMainWindow
from win32api import mouse_event

from InterfaceUI2 import *


class InterfaceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # self.ui.pushButton_8.clicked.connect(self.restore_or_maximize_window)
        self.ui.pushButton_15.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_16.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_17.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_18.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.pushButton_19.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.show()


# 鼠标拖拽事件
def mousePressEvent(self, event):
    if event.buttons() == Qt.LeftButton and self.isMaximized() == False:
        self.m_flag = True
        self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口位置
        event.accept()
        self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标


def mouseMoveEvent(self, event):
    if Qt.LeftButton and self.m_flag:
        self.move(mouse_event.globalPos() - self.m_DragPosition)  # 更改窗口位置
        mouse_event.accept()


def mouseReleaseEvent(self, mouse_event):
    self.m_drag = False
    self.setCursor(QCursor(Qt.ArrowType))


# 放大缩小
def restore_or_maximize_window(self):
    if self.isMaximized():
        self.showNormal()
        # self.ui.pushButton_8.setIcon(QIcon(u":/icons/icons/maxsize.png"))
        self.ui.pushButton_8.setIcon(QIcon(u":/icons/icons/最大化.png"))
    else:
        self.showMaximized()
        # self.ui.pushButton_8.setIcon(QIcon(u":/icons/icons/minisize.png"))
        self.ui.pushButton_8.setIcon(QIcon(u":/icons/icons/最小化.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = InterfaceWindow()
    sys.exit(app.exec())
