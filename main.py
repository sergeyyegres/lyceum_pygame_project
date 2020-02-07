import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
import breakout
import pygame
from pygame.locals import *
import sys
from breakout_sprites import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main1.ui', self)
        # get values
        with open('save.txt', 'rt') as f:
            a = f.read()
            values = [i for i in a.split('\n')]
        self.lineEdit.setText(values[0])
        self.lineEdit_2.setText(values[1])
        self.lineEdit_3.setText(values[2])
        self.lineEdit_4.setText(values[3])
        self.lineEdit_5.setText(values[4])
        self.lineEdit_6.setText(values[5])
        self.lineEdit_7.setText(values[6])
        self.lineEdit_8.setText(values[7])
        self.lineEdit_9.setText(values[8])
        self.WINDOW_WIDTH = self.lineEdit.text()
        self.WINDOW_HEIGHT = self.lineEdit_2.text()
        self.PLAYER_SPEED = self.lineEdit_3.text()
        self.BALL_SPEED = self.lineEdit_4.text()
        self.MOTION = self.lineEdit_5.text()
        self.STACK = self.lineEdit_6.text()
        self.START_DELAY = self.lineEdit_7.text()
        self.CLICK_DELAY = self.lineEdit_8.text()
        self.pushButton.clicked.connect(self.start)
        self.listWidget.clear()
        with open('history.txt', 'rt') as f:
            a = f.read()
            data = [i for i in a.split('\n')]
        for i in data[-2::-1]:
            self.listWidget.addItem(str(i))
        self.setWindowTitle('Breakout')

    def start(self):
        ex.close()
        self.WINDOW_WIDTH = self.lineEdit.text()
        self.WINDOW_HEIGHT = self.lineEdit_2.text()
        self.PLAYER_SPEED = self.lineEdit_3.text()
        self.BALL_SPEED = self.lineEdit_4.text()
        self.MOTION = self.lineEdit_5.text()
        self.STACK = self.lineEdit_6.text()
        self.START_DELAY = self.lineEdit_7.text()
        self.CLICK_DELAY = self.lineEdit_8.text()
        with open('save.txt', 'w') as f:
            f.write(self.WINDOW_WIDTH + '\n')
            f.write(self.WINDOW_HEIGHT + '\n')
            f.write(self.PLAYER_SPEED + '\n')
            f.write(self.BALL_SPEED + '\n')
            f.write(self.MOTION + '\n')
            f.write(self.STACK + '\n')
            f.write(self.START_DELAY + '\n')
            f.write(self.CLICK_DELAY + '\n')
            f.write(self.lineEdit_9.text() + '\n')
        breakout.game(int(self.WINDOW_WIDTH), int(self.WINDOW_HEIGHT), int(self.PLAYER_SPEED), int(self.MOTION),
                      int(self.STACK), int(self.START_DELAY), int(self.CLICK_DELAY), self.lineEdit_9.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
