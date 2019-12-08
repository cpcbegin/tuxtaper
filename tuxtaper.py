import PyQt5.QtCore as C
import os, sys, re
from tuxtaperui import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import pygame
from pygame.locals import *
from tkinter import messagebox


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_FormMain()
        self.ui.setupUi(self)
        self.sound_running = False
        self.sound_paused = False

        self.ui.pushButtonRecord.clicked.connect(self.press_record)
        self.ui.pushButtonPlay.clicked.connect(self.press_play)
        self.ui.pushButtonRewind.clicked.connect(self.press_rewind)
        self.ui.pushButtonAdvance.clicked.connect(self.press_advance)
        self.ui.pushButtonStop.clicked.connect(self.press_stop)
        self.ui.pushButtonPause.clicked.connect(self.press_pause)

    def press_record(self):
        messagebox.showinfo("Warning", "Record: NOT IMPLEMENTED YET")
        print("Record: NOT IMPLEMENTED YET")

    def press_play(self):
        if (pygame.mixer.music.load(self.ui.labelFilename.text()) != ""):
            pygame.mixer.music.load(self.ui.labelFilename.text())
            pygame.mixer.music.play(1)
            self.sound_running = True
            self.ui.labelTape.setPixmap(QPixmap("graphics/cassetteplay.gif"))
            print("play")

    def press_rewind(self):
        if self.sound_running:
            pygame.mixer.music.rewind()

    def press_advance(self):
        if self.sound_running:
            pygame.mixer.music.forward()

    def press_stop(self):
        if self.sound_running:
            pygame.mixer.music.stop()
            self.sound_running = False
            self.sound_paused = False
            self.ui.labelFilename.setText("")
            self.ui.labelTape.setPixmap(QPixmap("graphics/cassetteempty.jpg"))
        else:
            filter: object
            filename, filter = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", ".")
            self.ui.labelTape = QtWidgets.QLabel(self.ui.labelTape)
            if filename == "":
                self.ui.labelTape.setPixmap(QPixmap("graphics/cassetteempty.jpg"))
            else:
                self.ui.labelTape.setPixmap(QPixmap("graphics/cassettefull.jpg"))
            self.ui.labelTape.show()
            self.ui.labelFilename.setText(filename)

    def press_pause(self):
        if self.sound_paused:
            pygame.mixer.music.unpause()
            self.sound_paused = False
            print("despausado")
        else:
            pygame.mixer.music.pause()
            self.sound_paused = True
            print("pausado")


if __name__ == "__main__":
    pygame.init()

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    pygame.mixer.quit()