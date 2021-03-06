import mimetypes
import re
import sys
import subprocess
import pathlib

import PyQt5.QtCore as C
import pygame
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox
from pygame.locals import *
from tuxtaperui import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_FormMain()
        self.ui.setupUi(self)
        self.mime_tzx = [".cdt", ".tzx"]
        self.mime_cas = [".cas"]
        self.sound_running = False
        self.sound_paused = False
        self.vocfile = ""
        self.wavfile = ""

        self.ui.pushButtonRecord.clicked.connect(self.press_record)
        self.ui.pushButtonPlay.clicked.connect(self.press_play)
        self.ui.pushButtonRewind.clicked.connect(self.press_rewind)
        self.ui.pushButtonAdvance.clicked.connect(self.press_advance)
        self.ui.pushButtonStop.clicked.connect(self.press_stop)
        self.ui.pushButtonPause.clicked.connect(self.press_pause)

    def command_player(self, filename):
        self.vocfile = pathlib.PurePath(filename).with_suffix(".VOC")
        self.wavfile = pathlib.PurePath(filename).with_suffix(".wav")
        tape_extension = {
            ".cdt": [["playtzx", filename, "-voc"],
                    ["sox", "-t", "voc", self.vocfile,
                    pathlib.PurePath(filename).with_suffix(".wav")]],
            ".tzx": [["playtzx", filename, "-voc"],
                    ["sox", "-t", "voc", self.vocfile,
                     pathlib.PurePath(filename).with_suffix(".wav")]],
            ".tap": [["ubercassette", filename, self.wavfile]],
            ".cas": [["cas2wav", filename, self.wavfile]]
        }
        extension = pathlib.Path(filename).suffix.lower()
        if str(mimetypes.guess_type(filename)).find("audio") >= 0:
            self.ui.labelTape.setPixmap(QPixmap("graphics/cassettefull.jpg"))
            self.ui.labelTape.show()
            self.ui.labelFilename.setText(filename)
        elif extension in tape_extension:
            for tape_commands in tape_extension[extension]:
                subprocess.run(tape_commands)
            self.ui.labelTape.setPixmap(QPixmap("graphics/cassettefull.jpg"))
            self.ui.labelTape.show()
            self.ui.labelFilename.setText(str(self.wavfile))
            self.inputfile = self.wavfile;
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("NO ES UN ARCHIVO DE AUDIO " + extension)
            x = msg.exec_()

    def press_record(self):
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("Record: NOT IMPLEMENTED YET")
        x = msg.exec_()

    def press_play(self):
        if self.ui.labelFilename.text() != "":
            pygame.mixer.music.load(self.ui.labelFilename.text())
            pygame.mixer.music.play(1)
            self.sound_running = True
            self.ui.labelTape.setPixmap(QPixmap("graphics/cassetteplay.gif"))

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
                self.ui.labelTape.show()
            else:
                self.command_player(filename)

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