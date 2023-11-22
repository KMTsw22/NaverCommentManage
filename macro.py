import time
import math
import sys
from PyQt5.QtWidgets import *
from selenium.webdriver import ActionChains
import math

from PyQt5 import uic
from selenium.webdriver.common.by import By
from selenium import webdriver
from twocaptcha import TwoCaptcha

from PyQt5.QtCore import *


class Macro(QThread):
    def __init__(self, driver, Rest, Want, Now):
        super().__init__()
        self.running = True
        self.Can = True
        self.driver = driver
        self.Rest = Rest
        self.Want = Want
        self.Now = Now
        self.WantPercent = 100.0
        if self.Want.text() != "":
            self.WantPercent = float(self.Want.text())
    def run(self):
        try:
            self.driver.get(f'https://kin.naver.com/myinfo/answerList.naver?page=1')
            time.sleep(1.5)
            try:
                popup = self.driver.find_elements(By.XPATH,'/html/body/div[2]/div[4]/div[1]/div/div/a[1]')
                if len(popup) == 0:
                    pass
                else:
                    popup[0].click()
            except Exception as e:
                pass
            total=self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div[3]/dl[2]/dd[1]').text
            minus= self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div[3]/dl[2]/dd[1]/span').text
            total = total.replace(',', '')
            total = total.replace(' ', '')
            minus = minus.replace(',', '')
            minus = minus.replace(' ', '')
            LastPage = total[:len(total)-len(minus)]
            LastPage = int(LastPage)
            LastPage = math.ceil(LastPage / 20)
            while LastPage >= 1:
                try:
                    if not self.running:
                        break

                    self.Rest.setText(f"{LastPage}")
                    time.sleep(0.3)
                    self.driver.get(f'https://kin.naver.com/myinfo/answerList.naver?page={LastPage}')
                    Board = self.driver.find_element(By.ID,'au_board_list')
                    TitleList = self.driver.find_elements(By.CLASS_NAME,'title')
                    StatusList = self.driver.find_elements(By.CLASS_NAME,'field2')
                    list_ = []
                    for i in StatusList:
                        list_.append(i.text)
                    TitleList= TitleList[::-1]
                    list_ = list_[::-1]
                    for i in range(len(list_)):
                        try:
                            now_percent = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div[3]/dl[2]/dd[3]/div/span').text
                            now_percent = float(now_percent[:len(now_percent)-1])
                            self.Now.setText(str(now_percent))
                            time.sleep(0.1)
                            if now_percent >= self.WantPercent:
                                self.running = False
                                time.sleep(1.5)
                                self.Now.setText("완료")
                            if not self.running:
                                break
                            time.sleep(0.1)
                            if list_[i] != "완료":
                                continue
                            else:
                                self.driver.find_element(By.XPATH,f'/html/body/div[2]/div[3]/div/div/div[3]/table/tbody/tr[{len(list_)-i}]/td[2]/a').click()
                                time.sleep(1)
                                URL = self.driver.current_url.split('#')[-1]
                                num = URL[6:]
                                answer_num = URL[:6] + '_' + URL[6:]

                                try:
                                    while True:
                                        a_element = self.driver.find_element(By.ID,'nextPageButton')
                                        display_value = a_element.get_attribute('style')
                                        # "display" 속성이 "none"인지 확인합니다.
                                        if 'display: none' in display_value:
                                            break
                                        else:
                                            a_element.click()
                                            time.sleep(1.5)

                                    now_answer = self.driver.find_element(By.ID,f'{answer_num}')

                                    now_button = now_answer.find_element(By.ID, f'answerMenuButton{num}')
                                    actions = ActionChains(self.driver)
                                    # 요소까지 스크롤
                                    actions.move_to_element(now_button).perform()
                                    time.sleep(1)
                                    now_button.click()

                                    time.sleep(1)
                                    now_answer.find_element(By.ID,f'optDelete{num}').click()
                                    time.sleep(1)

                                    alert = self.driver.switch_to.alert
                                    time.sleep(1)
                                    alert.accept()
                                    self.driver.back()
                                    time.sleep(1)

                                except Exception as e:
                                    print(e)
                                    self.driver.back()
                                    time.sleep(1)
                        except Exception as e:
                            print(e)
                    LastPage -= 1
                except Exception as e:
                    print(e)
            pass
            print("finish")
        except Exception as e:
            print(e)

    def resume(self):
        self.running = True

    def pause(self):
        self.running = False
