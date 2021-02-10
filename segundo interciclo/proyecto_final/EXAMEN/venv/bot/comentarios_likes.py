from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import sys
import win32clipboard
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.common.exceptions import NoSuchElementException
import csv



class comentarios_likes():
    def __init__(self, driver, url, username, password,url_publicacion):
        self.driver = webdriver.Chrome(driver)
        self.driver.get(url)
        self.login(username,password)
        self.recolectar(url_publicacion)
        self.driver.quit()


    def ecepciones(self,e):
        print(e)
        self.driver.quit()
        sys.exit()

    def login(self, username, password):
        try:
            self.driver.maximize_window()
            #self.driver.switch_to.frame(0)
            time.sleep(3)
            email_box = self.driver.find_element_by_id('email')
            email_box.send_keys(username)

            pass_box = self.driver.find_element_by_id('pass')
            pass_box.send_keys(password)

            login_btn_box = self.driver.find_element_by_id('u_0_b')
            login_btn_box.click()
        except NoSuchElementException as e:
            self.ecepciones(e)
        except Exception as e:
            self.ecepciones(e)

    def recolectar(self,url_publicacion):
        time.sleep(5)
        self.driver.get(url_publicacion)

        comentarios = []
        """time.sleep(5)
        counter = self.driver.find_element_by_xpath('').get_attribute('innerHTML')
        print(count)"""

        time.sleep(5)
        lista_comentarios = self.driver.find_elements(
            By.XPATH,
            "//div[@style='text-align: start;']"
        )

        lista_usuarios = self.driver.find_elements(
            By.XPATH,
            "//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8']"
        )

        for usuario, comentario in zip(lista_usuarios, lista_comentarios):
            comentarios.append({"usuario": usuario.text, "comentario": comentario.text})

        time.sleep(10)
        self.driver.quit()

        informe = open("D:/Users/leand/PycharmProjects/EXAMEN/venv/bot/comentarios_likes.csv", "w")
        escritor = csv.DictWriter(informe, fieldnames=["usuario", "comentario"])
        escritor.writeheader()
        escritor.writerows(comentarios)
