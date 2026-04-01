# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InterfaceUI2.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1152, 655)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1071, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	background-color: rgb(198, 47, 47);\n"
"}\n"
"QPushButton, #pushButton {\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	padding-bottom: 4px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setFamilies([u"\u5e7c\u5706"])
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/\u7f51\u6613\u4e91\u97f3\u4e50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(60, 16777215))
        self.frame_6.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid rgb(74, 74, 74)\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/\u540e\u9000.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/\u524d\u8fdb.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 30))
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(250, 30))
        self.lineEdit.setMaximumSize(QSize(250, 16777215))
        self.lineEdit.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgba(0, 0, 0, 80);\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 7px;")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.frame_7, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_4 = QPushButton(self.frame_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/\u4e2a\u4eba.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.horizontalLayout.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_5 = QPushButton(self.frame_9)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/\u76ae\u80a4.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_5)

        self.pushButton_7 = QPushButton(self.frame_9)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/\u90ae\u7bb1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.frame_9)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/\u8bbe\u7f6e.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_6)


        self.horizontalLayout.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(110, 0))
        self.frame_10.setMaximumSize(QSize(110, 16777215))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.line = QFrame(self.frame_10)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(1, 16777215))
        self.line.setStyleSheet(u"background-color: rgb(118, 118, 118);")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_6.addWidget(self.line)

        self.pushButton_8 = QPushButton(self.frame_10)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/\u6700\u5c0f\u5316.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_10)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/\u6700\u5927\u5316.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_10)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/\u5173\u95ed.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon9)
        self.pushButton_10.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.pushButton_10)


        self.horizontalLayout.addWidget(self.frame_10, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(5)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy2)
        self.frame_14.setMinimumSize(QSize(219, 0))
        self.frame_14.setMaximumSize(QSize(219, 16777215))
        self.frame_14.setStyleSheet(u"#frame_14 {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(98, 98, 98);\n"
"}\n"
"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QPushButton:focus {\n"
"	background-color: rgb(176, 176, 176);\n"
"}")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_14)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 60))
        self.frame_16.setMaximumSize(QSize(16777215, 60))
        self.frame_16.setStyleSheet(u"color: rgb(122, 122, 122);")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_16)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_5.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_17)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.line_3 = QFrame(self.frame_17)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_3)

        self.pushButton_15 = QPushButton(self.frame_17)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(217, 50))
        self.pushButton_15.setMaximumSize(QSize(217, 50))

        self.verticalLayout_6.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.frame_17)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(217, 50))
        self.pushButton_16.setMaximumSize(QSize(217, 50))

        self.verticalLayout_6.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.frame_17)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(217, 50))
        self.pushButton_17.setMaximumSize(QSize(217, 50))

        self.verticalLayout_6.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.frame_17)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(217, 50))
        self.pushButton_18.setMaximumSize(QSize(217, 50))

        self.verticalLayout_6.addWidget(self.pushButton_18)

        self.pushButton_19 = QPushButton(self.frame_17)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(217, 50))
        self.pushButton_19.setMaximumSize(QSize(217, 50))

        self.verticalLayout_6.addWidget(self.pushButton_19)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.verticalLayout_5.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 60))
        self.frame_18.setMaximumSize(QSize(16777215, 60))
        self.frame_18.setStyleSheet(u"color: rgb(122, 122, 122);")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_18)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_5.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_19)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.frame_19)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.pushButton_20 = QPushButton(self.frame_19)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(217, 50))
        self.pushButton_20.setMaximumSize(QSize(217, 50))

        self.verticalLayout_7.addWidget(self.pushButton_20)

        self.pushButton_21 = QPushButton(self.frame_19)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(217, 50))
        self.pushButton_21.setMaximumSize(QSize(217, 50))

        self.verticalLayout_7.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.frame_19)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(217, 50))
        self.pushButton_22.setMaximumSize(QSize(217, 50))

        self.verticalLayout_7.addWidget(self.pushButton_22)


        self.verticalLayout_5.addWidget(self.frame_19)


        self.horizontalLayout_10.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(4)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy3)
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_15)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_14 = QHBoxLayout(self.page)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(802, 494))
        self.label_4.setMaximumSize(QSize(802, 494))
        self.label_4.setStyleSheet(u"border-image: url(:/images/images/image1.jpg);")

        self.horizontalLayout_14.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_16 = QHBoxLayout(self.page_3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(802, 494))
        self.label_6.setMaximumSize(QSize(802, 494))
        self.label_6.setStyleSheet(u"border-image: url(:/images/images/image1.jpg);")

        self.horizontalLayout_16.addWidget(self.label_6)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_17 = QHBoxLayout(self.page_4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(802, 494))
        self.label_7.setMaximumSize(QSize(802, 494))
        self.label_7.setStyleSheet(u"border-image: url(:/images/images/image1.jpg);")

        self.horizontalLayout_17.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.horizontalLayout_18 = QHBoxLayout(self.page_5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(802, 494))
        self.label_8.setMaximumSize(QSize(802, 494))
        self.label_8.setStyleSheet(u"border-image: url(:/images/images/image1.jpg);")

        self.horizontalLayout_18.addWidget(self.label_8)

        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_15 = QHBoxLayout(self.page_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(802, 494))
        self.label_5.setMaximumSize(QSize(802, 494))
        self.label_5.setStyleSheet(u"border-image: url(:/images/images/image2.jpg);")

        self.horizontalLayout_15.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_13.addWidget(self.stackedWidget)


        self.horizontalLayout_10.addWidget(self.frame_15)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setStyleSheet(u"#frame_4 {\n"
"	background-color: rgb(246, 246, 248);\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(200, 16777215))
        self.frame_11.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(198, 47, 47);\n"
"	border: none;\n"
"	border-radius: 22px;\n"
"}\n"
"QPushButton:pressed {\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"}")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.frame_11)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(45, 45))
        self.pushButton_11.setMaximumSize(QSize(45, 45))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon10)
        self.pushButton_11.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_11)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(45, 45))
        self.pushButton_12.setMaximumSize(QSize(45, 45))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/next.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon11)
        self.pushButton_12.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.pushButton_12)


        self.horizontalLayout_7.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_12)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(550, 0))
        self.label.setStyleSheet(u"background-image: url(:/images/images/bar.png);")

        self.verticalLayout_4.addWidget(self.label)


        self.horizontalLayout_7.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QPushButton, #pushButton {\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	padding-bottom: 4px;\n"
"}")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.frame_13)
        self.pushButton_13.setObjectName(u"pushButton_13")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/\u97f3\u4e50\u5217\u8868-copy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_13.setIcon(icon12)
        self.pushButton_13.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame_13)
        self.pushButton_14.setObjectName(u"pushButton_14")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/\u6b4c\u8bcd.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_14.setIcon(icon13)
        self.pushButton_14.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.pushButton_14)


        self.horizontalLayout_7.addWidget(self.frame_13)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_10.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u6613\u4e91\u97f3\u4e50", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u97f3\u4e50\uff0c\u89c6\u9891\uff0c\u6b4c\u8bcd\uff0c\u7535\u53f0", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u" XXL", None))
        self.pushButton_5.setText("")
        self.pushButton_7.setText("")
        self.pushButton_6.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
        self.pushButton_10.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u63a8\u8350", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u73b0\u97f3\u4e50", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u79c1\u4ebaFM", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Look\u76f4\u64ad", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u670b\u53cb", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6211\u7684\u97f3\u4e50", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u97f3\u4e50", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"\u6211\u7684\u6536\u85cf", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"\u6211\u7684\u559c\u6b22", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.label.setText("")
        self.pushButton_13.setText("")
        self.pushButton_14.setText("")
    # retranslateUi

