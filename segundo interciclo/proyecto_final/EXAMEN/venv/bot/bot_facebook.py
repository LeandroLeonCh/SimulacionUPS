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




class bot_facebook():
    def __init__(self, driver, url, username, password):
        self.driver = webdriver.Chrome(driver)
        self.driver.get(url)
        self.login(username, password)
        self.publicar_flyer()
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


    def publicar_flyer (self):
        image_path = 'C:/Users/leand/Downloads/VOTA-12IDflyer_examen.png'
        # time.sleep(5)
        try:

            time.sleep(10)
            self.driver.find_element(By.CSS_SELECTOR, ".jm1wdb64 > .a8c37x1j").click()

            time.sleep(5)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//*[@id='mount_0_0']/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[1]/div[2]/div/div[1]/input"
                ))).send_keys(image_path)

            time.sleep(5)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//*[@id='mount_0_0']/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div"
                ))).click()
        except NoSuchElementException as e:
            self.ecepciones(e)
        except Exception as e:
            self.ecepciones(e)