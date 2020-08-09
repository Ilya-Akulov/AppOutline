# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TrySecond.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2 import QtGui
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PIL import Image
from PIL.ImageQt import ImageQt
from Operators import Oper


class Ui_Dialog(Oper):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1366, 768)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(830, 560, 201, 71))
        self.pushButton.setIconSize(QSize(16, 16))

        self.pushButton_1 = QPushButton(Dialog)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(20, 560, 201, 71))
        self.pushButton_1.setIconSize(QSize(16, 16))

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(290, 560, 201, 71))
        self.pushButton_2.setIconSize(QSize(16, 16))

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(560, 560, 201, 71))

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 552, 471))#20, 30, 563, 200
        self.label.setPixmap(QPixmap(u":/newPrefix/test.qrc"))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(720, 30, 552, 471))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/test.qrc"))

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Outline", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Open file", None))
        self.pushButton_1.setText(QCoreApplication.translate("Dialog", u"Laplas", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Roberts", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Sobel", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"№1", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"№2", None))
    # retranslateUi

        # Выбор файла !!!!!!!!!!!!!!!!!!!!! пригодится для картинки
    def openFile(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        #print(self.path)
        self.scale_image()

    def scale_image(self):
        self.picture = QPixmap(self.path)

        self.original_image = Image.open(self.path)
        self.width_s, self.height_s = self.label.width(), self.label.height()
        self.sizePic = (self.width_s, self.height_s)

        self.resized_image = self.original_image.resize(self.sizePic)
        self.qim = ImageQt(self.resized_image)
        self.pix = QtGui.QPixmap.fromImage(self.qim)
        self.label.setPixmap(QPixmap(self.pix))
        # return self.resized_image

    def pushButtonClick1(self):
        self.pic = self.mainInOper(self.original_image, 1)
        self.newPic = self.pic.resize(self.sizePic)
        self.qim = ImageQt(self.newPic)
        self.pix = QtGui.QPixmap.fromImage(self.qim)
        self.label_2.setPixmap(QPixmap(self.pix))

    def pushButtonClick2(self):
        self.pic = self.mainInOper(self.original_image, 2)
        self.newPic = self.pic.resize(self.sizePic)
        self.qim = ImageQt(self.newPic)
        #self.qim = ImageQt(self.mainInOper(self.resized_image, 2))
        self.pix = QtGui.QPixmap.fromImage(self.qim)
        self.label_2.setPixmap(QPixmap(self.pix))

    def pushButtonClick3(self):
        self.pic = self.mainInOper(self.original_image, 3)
        self.newPic = self.pic.resize(self.sizePic)
        self.qim = ImageQt(self.newPic)
        #self.qim = ImageQt(self.mainInOper(self.resized_image, 3))
        self.pix = QtGui.QPixmap.fromImage(self.qim)
        self.label_2.setPixmap(QPixmap(self.pix))

    def pushButtonClick(self):
        self.pushButton.clicked.connect(self.openFile)
        self.pushButton_1.clicked.connect(self.pushButtonClick1)
        self.pushButton_2.clicked.connect(self.pushButtonClick2)
        self.pushButton_3.clicked.connect(self.pushButtonClick3)


