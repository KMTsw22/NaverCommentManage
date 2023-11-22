import time
import math
import sys
from PyQt5.QtWidgets import *
from selenium.webdriver import ActionChains

from PyQt5 import uic
from selenium.webdriver.common.by import By
from selenium import webdriver

from PyQt5.QtCore import *



class login(QThread):
    def __init__(self, driver):
        super().__init__()
        self.running = True
        self.Can = True
        self.driver = driver

    def run(self):
        try:
            self.driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/')
            # self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[1]/div[1]/input').send_keys('ghrmsdla1004')
            # self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[1]/div[2]/input').send_keys('zmahd1234!')

            pass

        except Exception as e:
            print(e)

    def resume(self):
        self.running = True

    def pause(self):
        self.running = False
