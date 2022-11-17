# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'render_log_viewer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        if not mainwindow.objectName():
            mainwindow.setObjectName(u"mainwindow")
        mainwindow.resize(484, 547)
        self.centralwidget = QWidget(mainwindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.filepath = QLineEdit(self.centralwidget)
        self.filepath.setObjectName(u"filepath")
        self.filepath.setGeometry(QRect(10, 30, 351, 20))
        self.browsebutton = QPushButton(self.centralwidget)
        self.browsebutton.setObjectName(u"browsebutton")
        self.browsebutton.setGeometry(QRect(374, 29, 75, 23))
        self.warninglabel = QLabel(self.centralwidget)
        self.warninglabel.setObjectName(u"warninglabel")
        self.warninglabel.setGeometry(QRect(10, 70, 61, 21))
        self.warningbox = QPlainTextEdit(self.centralwidget)
        self.warningbox.setObjectName(u"warningbox")
        self.warningbox.setGeometry(QRect(10, 90, 441, 161))
        self.errorbox = QPlainTextEdit(self.centralwidget)
        self.errorbox.setObjectName(u"errorbox")
        self.errorbox.setGeometry(QRect(10, 280, 441, 91))
        self.infobox = QPlainTextEdit(self.centralwidget)
        self.infobox.setObjectName(u"infobox")
        self.infobox.setGeometry(QRect(10, 410, 441, 71))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 260, 47, 13))
        self.infolabel = QLabel(self.centralwidget)
        self.infolabel.setObjectName(u"infolabel")
        self.infolabel.setGeometry(QRect(10, 390, 161, 16))
        self.logfilelabel = QLabel(self.centralwidget)
        self.logfilelabel.setObjectName(u"logfilelabel")
        self.logfilelabel.setGeometry(QRect(10, 10, 47, 13))
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainwindow)
        self.statusbar.setObjectName(u"statusbar")
        mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwindow)

        QMetaObject.connectSlotsByName(mainwindow)
    # setupUi

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(QCoreApplication.translate("mainwindow", u"Render Log Analysis", None))
        self.browsebutton.setText(QCoreApplication.translate("mainwindow", u"Browse", None))
        self.warninglabel.setText(QCoreApplication.translate("mainwindow", u"Warnings", None))
        self.label.setText(QCoreApplication.translate("mainwindow", u"Errors", None))
        self.infolabel.setText(QCoreApplication.translate("mainwindow", u"Info", None))
        self.logfilelabel.setText(QCoreApplication.translate("mainwindow", u"Log file", None))
    # retranslateUi

