import time
import math
import sys
from PyQt5.QtWidgets import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

from PyQt5 import uic
from Login import login
from Ui import Ui_Dialog
from PyQt5.QtCore import *
from macro import Macro
app = QApplication(sys.argv)

# form_class = uic.loadUiType("LoginUi.ui")[0]


class MyWindow(QMainWindow, Ui_Dialog):
    progress_start = pyqtSignal(int)
    progress_finish = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.selen = None
        self.setupUi(self)
        self.StartBtn.clicked.connect(self.resume)
        self.FinishBtn.clicked.connect(self.pause)
        self.MacroBtn.clicked.connect(self.StartMacro)
        self.driver = webdriver.Chrome()

    def resume(self):
        self.Login = login(self.driver)
        self.Login.start()


    def StartMacro(self):
        self.macro = Macro(self.driver, self.Rest, self.Want, self.Now)
        time.sleep(1)
        self.macro.start()
        time.sleep(1)



    def pause(self):
        self.macro.pause()
        while True:
            if not self.macro.running:
                time.sleep(3)
                self.show_alert("작업이 중지되었습니다.")
                break
    def show_alert(self, text):
        alert = QMessageBox()
        alert.setWindowTitle("알림")
        alert.setText(text)
        alert.setIcon(QMessageBox.Information)
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec_()


if __name__ == "__main__":
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())

# python -m PyQt5.uic.pyuic -x LoginUi.ui -o Ui.py
# python -m PyInstaller --onefile --noconsole main.py