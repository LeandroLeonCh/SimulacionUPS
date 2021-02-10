from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys

class excel_bot():
    def __init__(self, driver, url, username, password):
        self.driver = webdriver.Chrome(driver)
        self.driver.get(url)
        self.login(username, password)


    def ecepciones(self,e):
        print(e)
        self.driver.quit()
        sys.exit()

    def subir_correos(self, username, password):
        try:

            self.driver.maximize_window()
            email_box = self.driver.find_element_by_id('email')
            email_box.send_keys(username)

            pass_box = self.driver.find_element_by_id('pass')
            pass_box.send_keys(password)

            login_btn_box = self.driver.find_element_by_id('u_0_b')
            login_btn_box.click()

        except NoSuchElementException as e:
            self.ecepciones(e)
        except Exception as e:
            self.ecepciones(e)'''


