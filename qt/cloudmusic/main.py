import sys

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from InterfaceUi2 import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from win32api import mouse_event


class InterfaceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = InterfaceWindow()


# 鼠标拖拽事件
def mousePressEvent(self, event):
    if event.buttons() == QtCore.Qt.LeftButton and self.isMaximized() == False:
        self.m_flag = True
        self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口位置
        event.accept()
        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标


def mouseMoveEvent(self, event):
    if QtCore.Qt.LeftButton and self.m_flag:
        self.move(mouse_event.globalPos() - self.m_DragPosition)  # 更改窗口位置
        mouse_event.accept()


def mouseReleaseEvent(self, mouse_event):
    self.m_drag = False
    self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowType))
