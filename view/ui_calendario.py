# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_calendarioKMsnhM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Calendario(object):
    def setupUi(self, Calendario):
        if not Calendario.objectName():
            Calendario.setObjectName(u"Calendario")
        Calendario.resize(632, 515)
        self.centralwidget = QWidget(Calendario)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(25)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(40, 40, 40, 40)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size:25px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.calendario = QCalendarWidget(self.centralwidget)
        self.calendario.setObjectName(u"calendario")
        self.calendario.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        self.gridLayout.addWidget(self.calendario, 1, 0, 1, 1)

        Calendario.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calendario)

        QMetaObject.connectSlotsByName(Calendario)
    # setupUi

    def retranslateUi(self, Calendario):
        Calendario.setWindowTitle(QCoreApplication.translate("Calendario", u"Estructura QCalendarWidget - ALEX7320", None))
        self.label.setText(QCoreApplication.translate("Calendario", u"QCalendarWidget (Estructura)", None))
    # retranslateUi

