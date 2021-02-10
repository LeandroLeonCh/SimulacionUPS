from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.common.exceptions import NoSuchElementException

class flyer_bot():
    def __init__(self, driver, url):
        self.driver = webdriver.Chrome(driver)
        self.driver.get(url)
        self.vars = {}
        self.login_canvas()
        self.driver.quit()

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def ecepciones(self,e):
        print(e)
        #self.driver.quit()
        #sys.exit()

    def login_canvas(self):
        try:
            self.driver.maximize_window()
            self.driver.switch_to.frame(0)
            self.driver.find_element(By.ID, "main_menu_0_0").click()
            self.driver.find_element(By.ID, "main_menu_1_2").click()
            self.driver.find_element(By.ID, "main_menu_2_0").click()
            self.driver.find_element(By.ID, "file_open").send_keys(
                'D:/Users/leand/PycharmProjects/EXAMEN/venv/bot/VOTA 12ID.jpg')
            self.driver.find_element(By.ID, "main_menu_0_0").click()
            self.driver.find_element(By.ID, "main_menu_1_2").click()
            self.driver.find_element(By.ID, "main_menu_2_0").click()
            self.driver.find_element(By.ID, "file_open").send_keys(
                'D:/Users/leand/PycharmProjects/EXAMEN/venv/bot/12id.jpg')

            self.driver.find_element(By.ID, "canvas_minipaint").click()
            self.driver.find_element(By.ID, "main_menu_0_0").click()
            self.driver.find_element(By.ID, "main_menu_1_5").click()
            self.driver.find_element(By.ID, "pop_data_name").click()
            self.driver.find_element(By.ID, "pop_data_name").send_keys("flyer_examen")
            self.driver.find_element(By.ID, "popup_ok").click()

            time.sleep(5)
            self.driver.quit()
        except NoSuchElementException as e:
            self.ecepciones(e)
        except Exception as e:
            self.ecepciones(e)