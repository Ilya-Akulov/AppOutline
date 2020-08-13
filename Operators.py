from PIL import Image
from PIL.ImageDraw import Draw#ImageDraw #Подключим необходимые библиотеки.
from PySide2 import QtGui
import math as mh

class Oper(object):
    # Функция нахождения яркости пикселя
    def brightness(self,x, y):
        R, G, B = self.pix[x, y]
        return sum([R, G, B]) // 3  # 0 is dark (black) and 255 is bright (white)

    # Функция изменения цвета
    def changeColor(self,alpha, maska, x, y):
        for i in [x - 2, x - 1, x]:
            for j in [y - 3, y - 2, y - 1]:
                self.picture[i][j] = alpha

    # **************************************
    # Оператор Робертса
    def operRoberts(self,matrix, x, y):
        Gx = matrix[x + 1][y + 1] - matrix[x][y]
        Gy = matrix[x + 1][y] - matrix[x][y + 1]
        # G = np.sqrt(sum([Gx ** 2, Gy ** 2]))
        G = mh.fabs(Gx) + mh.fabs(Gy)
        return G

    # **************************************

    # **************************************
    # Оператор Собеля
    def operSobel(self,matrix, x, y):
        Gx = (matrix[x + 1][y - 1] + 2 * matrix[x + 1][y] + matrix[x + 1][y + 1]) - (
                    matrix[x - 1][y - 1] + 2 * matrix[x - 1][y] + matrix[x - 1][y + 1])
        Gy = (matrix[x - 1][y + 1] + 2 * matrix[x][y + 1] + matrix[x + 1][y + 1]) - (
                    matrix[x - 1][y - 1] + 2 * matrix[x][y - 1] + matrix[x + 1][y - 1])
        G = mh.sqrt(sum([Gx ** 2, Gy ** 2]))
        return G

    # **************************************

    # **************************************
    # Оператор Лапласа
    def operLaplas(self, matrix, x, y):
        Gx = 4 * matrix[x][y] - matrix[x - 1][y] - matrix[x][y - 1] - matrix[x][y + 1] - matrix[x + 1][y]
        Gy = 8 * matrix[x][y] - matrix[x - 1][y - 1] - matrix[x - 1][y] - matrix[x - 1][y + 1] - matrix[x][y - 1] - \
             matrix[x][y + 1] - matrix[x + 1][y - 1] - matrix[x + 1][y] - matrix[x + 1][y + 1]
        G = mh.sqrt(sum([Gx ** 2, Gy ** 2]))
        return G

    # **************************************

    # Функция выбора оператора
    def choiceOper(self, num):
        if (num == 1):
            self.changeColor(self.operLaplas(self.mask, 1, 1), self.mask, self._wid, self._hei)
        elif (num == 2):
            self.changeColor(self.operRoberts(self.mask, 1, 1), self.mask, self._wid, self._hei)
        elif(num == 3):
            self.changeColor(self.operSobel(self.mask, 1, 1), self.mask, self._wid,self._hei)


    def mainInOper(self, pict, num):

        self.image = pict#pict#Открываем изображение.
        self.width = self.image.size[0] #Определяем ширину.
        self.height = self.image.size[1] #Определяем высоту.
        self.mask = []#Маска со значениями яркости пикселя
        self.picture = []#Массив для записи градиентов точек

        # Маска 3х3
        for j in range(3):
            mask2 = []
            for i in range(3):
                mask2.append(0)
            self.mask.append(mask2)

        # Вспомогательный массив, который хранит яркости пикселей для нового изображения
        for j in range(self.width):
            picture2 = []
            for i in range(self.height):
                picture2.append(0)
            self.picture.append(picture2)

        # Подгонка изображения для матрицы 3х3
        if (self.width%3 != 0 and self.height%3 != 0):
            self.imag = self.image.crop((0,0,self.width - self.width%3, self.height - self.height%3))
        elif (self.width%3 != 0):
            self.imag = self.image.crop((0, 0, self.width - self.width%3, self.height))
        elif (self.height%3 != 0):
            self.imag = self.image.crop((0, 0, self.width, self.height - self.height % 3))
        else:
            self.imag = self.image

        self.draw = Draw(self.imag)#Создаем инструмент для рисования.
        self.width = self.imag.size[0] #Определяем ширину.
        self.height = self.imag.size[1] #Определяем высоту.
        self.pix = self.imag.load() #Выгружаем значения пикселей.

        print(self.imag.size)  # Размер изображения
        self._hei = 0  # Индекс для прохода по длине
        self._wid = 0  # Индекс для прохода по ширине
        self._i_wid = 0  # Индекс для прохода по ширине по маске (3x3)

        # Обход изображения применяя к нему маску выбранного оператора
        while self._wid < self.width:
            self._j_hei = 0  # Индекс для прохода по длне по маске (3x3)
            while self._hei < self.height and self._j_hei < 3:
                self.mask[self._i_wid][self._j_hei] = self.brightness(self._wid, self._hei)  # записываем значение яркости пикселя в маску
                self._j_hei += 1
                self._hei += 1
            if (self._i_wid == 2):
                if (self._hei == self.height):
                    # alph = math.atan(operRoberts(mask, 1, 1)) - угол
                    self.choiceOper(num)
                    self._hei = 0;
                    self._i_wid = 0
                    self._wid += 1
                else:
                    self.choiceOper(num)
                    # alph = math.atan(operRoberts(mask, 1, 1)) - угол
                    self._i_wid = 0
                    self._wid -= 2
            else:
                self._hei -= 3
                self._i_wid += 1
                self._wid += 1

            if (self._hei == self.height):
                self._hei = 0

        #Перерисовывание изображения новыми пикселями
        for i in range(self.width):
            for j in range(self.height):
                self.draw.point((i, j), (int(self.picture[i][j]), int(self.picture[i][j]), int(self.picture[i][j])))  # (a, b, c))
        return self.imag


        # self.pixel = QtGui.QImage(pict)
        #
        # self.painter = QtGui.QPainter()
        # # Перерисовывание изображения новыми пикселями
        # # for i in range(self.width):
        # #     for j in range(self.height):
        # #         self.painter.setPen(QtGui.QColor(int(self.picture[i][j]), int(self.picture[i][j]), int(self.picture[i][j])))
        # #         self.painter.drawImage(i, j,self.pix)
        # # return self.painter
        # for i in range(self.width):
        #     for j in range(self.height):
        #         print(self.picture[i][j])
        #         self.pixel.setPixel(i,j,0)#int(self.picture[i][j]))
        # return self.pixel





