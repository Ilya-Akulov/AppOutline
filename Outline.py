import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PIL import Image
from PIL.ImageQt import ImageQt
from PySide2.QtGui import QPixmap
from TrySecond import Ui_Dialog
#from Operators import Oper

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

#ui.openFile()# Выбор файла
ui.pushButtonClick()
#ui.scale_image()
app.exec_()
#sys.exit(app.exec_())