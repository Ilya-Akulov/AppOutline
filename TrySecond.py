from PySide2 import QtGui
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QFileDialog as qf
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
        self.pushButton_3.setIconSize(QSize(16, 16))

        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(1100, 560, 201, 71))
        self.pushButton_4.setIconSize(QSize(16, 16))

        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(1100, 650, 201, 71))
        self.pushButton_5.setIconSize(QSize(16, 16))

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
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Clear", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"№1", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"№2", None))
    # retranslateUi

    # Выбор файла
    def openFile(self):
        filename = qf.getOpenFileName()
        self.path = filename[0]

    # Функция  изменения исходной картинки под поле лейбла
    def scale_image(self):
        path = self.path
        self.picture = QPixmap(path)
        self.original_image = Image.open(path)
        self.al_image = QtGui.QImage(path)
        self.width_label, self.height_label = self.label.width(), self.label.height()
        self.sizePic = (self.width_label, self.height_label)
        print( self.sizePic)
        print(self.original_image.size)
        if (self.original_image.width > self.original_image.height):
                self.coefScaled = round(self.original_image.width/self.width_label)
        else: self.coefScaled = round(self.original_image.height/self.height_label)
        if self.coefScaled == 1: self.coefScaled = 1.5
        self.widImag,self.heighImag = self.original_image.width/self.coefScaled, self.original_image.height/self.coefScaled
        self.zed_imaged = self.al_image.scaled(self.widImag,self.heighImag)#делить на целое число во сколько раз картинка больше рамки
        self.pixx = QPixmap.fromImage(self.zed_imaged)
        self.label.setPixmap(self.pixx)

    # Нажатие на кнопку открыть файл, в ней происходит открытие файла и загрузка исходной картинки в первое поле
    def openImageAndPushInLabel(self):
        self.openFile()
        self.scale_image()

    #Нажатие на кнопку оператора Лапласа
    def pushButtonClick1(self):
        orig = self.original_image
        self.pic = self.mainInOper(orig,1)#(self.original_image, 1)
        self.newPic = self.pic.resize((int(self.widImag), int(self.heighImag)))
        self.qim = ImageQt(self.newPic)
        self.pix = QPixmap.fromImage(self.qim)
        self.label_2.clear()
        self.label_2.setPixmap(self.pix)


    # Нажатие на кнопку оператора Робертса
    def pushButtonClick2(self):
        orig = self.original_image
        self.pic = self.mainInOper(orig, 2)
        #self.pic = self.mainInOper(self.original_image, 2)
        self.newPic = self.pic.resize((int(self.widImag), int(self.heighImag)))
        self.qim = ImageQt(self.newPic)
        self.pix = QPixmap.fromImage(self.qim)
        self.label_2.clear()
        self.label_2.setPixmap(self.pix)

    # Нажатие на кнопку оператора Собеля
    def pushButtonClick3(self):
        orig = self.original_image
        self.pic = self.mainInOper(orig, 3)
        #self.pic = self.mainInOper(self.original_image, 3)
        self.newPic = self.pic.resize((int(self.widImag), int(self.heighImag)))
        self.qim = ImageQt(self.newPic)
        self.pix = QPixmap.fromImage(self.qim)
        self.label_2.clear()
        self.label_2.setPixmap(self.pix)

    # Нажатие на кнопку очистки двух полей картинок
    def pushButtonClick4(self):
        self.label.clear()
        self.label_2.clear()

    # Нажатие на кнопку сохранение картинки с контурами
    def saveImage(self):
        fileNameSave = qf.getSaveFileName()
        self.pathSave = fileNameSave[0]+".jpg"
        self.pic.save(self.pathSave,"JPEG")

    # Функция объединяющая в себе все функции с кнопками
    def pushButtonClick(self):
        self.pushButton.clicked.connect(self.openImageAndPushInLabel)
        self.pushButton_1.clicked.connect(self.pushButtonClick1)
        self.pushButton_2.clicked.connect(self.pushButtonClick2)
        self.pushButton_3.clicked.connect(self.pushButtonClick3)
        self.pushButton_4.clicked.connect(self.pushButtonClick4)
        self.pushButton_5.clicked.connect(self.saveImage)




