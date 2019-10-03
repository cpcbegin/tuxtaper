import os, sys, re
from tuxtaperui import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_FormMain()
        self.ui.setupUi(self)

        self.ui.pushButtonRecord.clicked.connect(self.press_record)
        self.ui.pushButtonPlay.clicked.connect(self.press_play)
        self.ui.pushButtonRewind.clicked.connect(self.press_rewind)
        self.ui.pushButtonAdvance.clicked.connect(self.press_advance)
        self.ui.pushButtonStop.clicked.connect(self.press_stop)
        self.ui.pushButtonPause.clicked.connect(self.press_pause)

    def press_record(self):
        print("Record")

    def press_play(self):
        print("Play")

    def press_rewind(self):
        print("Rewind")

    def press_advance(self):
        print("Advance")

    def press_stop(self):
        filter: object
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", ".")
        self.ui.labelTape = QtWidgets.QLabel(self.ui.labelTape)
        if filename == "":
            self.ui.labelTape.setPixmap(QPixmap("graphics/cassetteempty.jpg"))
        else:
            self.ui.labelTape.setPixmap(QPixmap("graphics/cassettefull.jpg"))
        self.ui.labelTape.show()
        self.ui.labelFilename.setText(filename)
        print("Stop")

    def press_pause(self):
        print("Pause")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
