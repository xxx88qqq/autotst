# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1084, 729)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(91, 0))

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.spinBox = QSpinBox(self.groupBox_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(7)

        self.horizontalLayout.addWidget(self.spinBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.pushButton_16 = QPushButton(self.groupBox_2)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_5.addWidget(self.pushButton_16)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.toolButton = QToolButton(self.groupBox_3)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setAutoRaise(True)

        self.gridLayout_2.addWidget(self.toolButton, 0, 0, 1, 1)

        self.toolButton_2 = QToolButton(self.groupBox_3)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setArrowType(Qt.NoArrow)

        self.gridLayout_2.addWidget(self.toolButton_2, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pb_apply = QPushButton(self.groupBox_3)
        self.pb_apply.setObjectName(u"pb_apply")

        self.horizontalLayout_4.addWidget(self.pb_apply)

        self.pb_start = QPushButton(self.groupBox_3)
        self.pb_start.setObjectName(u"pb_start")

        self.horizontalLayout_4.addWidget(self.pb_start)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addWidget(self.groupBox_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.graphics_grid = QGridLayout()
        self.graphics_grid.setObjectName(u"graphics_grid")

        self.verticalLayout_8.addLayout(self.graphics_grid)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_log = QGroupBox(self.tab_3)
        self.groupBox_log.setObjectName(u"groupBox_log")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_log)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.textBrowser = QTextBrowser(self.groupBox_log)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"border-width: 0px;\n"
"border-style:outset;\n"
"")
        self.textBrowser.setLineWidth(0)

        self.verticalLayout_7.addWidget(self.textBrowser)


        self.verticalLayout.addWidget(self.groupBox_log)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 2)
        self.pushButton_15 = QPushButton(self.tab_3)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.pushButton_15)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_14 = QPushButton(self.tab_3)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_3.addWidget(self.pushButton_14)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u9879", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u4eea\u914d\u7f6e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IP\u5730\u5740", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"192.168.1.10", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u901a\u9053", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u63a7\u5236", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"\u6307\u4ee4\u6587\u4ef6...", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u5f62\u6587\u4ef6...", None))
        self.pb_apply.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pb_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u914d\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u7ed3\u679c", None))
        self.groupBox_log.setTitle(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\u4fe1\u606f", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u65e5\u5fd7", None))
    # retranslateUi

