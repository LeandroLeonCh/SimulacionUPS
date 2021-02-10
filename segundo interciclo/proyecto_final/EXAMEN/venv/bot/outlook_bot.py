import pyperclip
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



class outlook_bot():
    def __init__(self, driver, url, username, password):
        self.driver = webdriver.Chrome(driver)
        self.driver.get(url)
        self.login(username, password)
        self.driver.quit()



    def ecepciones(self,e):
        print(e)
        self.driver.quit()
        sys.exit()

    def login(self, username, password):
        correos = []
        try:
            self.driver.maximize_window()
            # self.driver.switch_to.frame(0)

            time.sleep(3)
            self.driver.find_element(By.ID, "i0116").click()
            self.driver.find_element(By.ID, "i0116").send_keys(username)
            self.driver.find_element(By.ID, "idSIButton9").click()

            time.sleep(3)
            self.driver.find_element(By.ID, "i0118").click()
            self.driver.find_element(By.ID, "i0118").send_keys(password)  #
            self.driver.find_element(By.ID, "idSIButton9").click()
            time.sleep(3)
            self.driver.find_element(By.ID, "idSIButton9").click()
            time.sleep(5)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div[3]/a/span/i').click()
            # self.driver.find_element_by_id("HubPersonaId_AAQkADc4YTU4NjRmLWJlZjUtNGE1Ny05ZTg1LTIyMDZlYmRmODcwNQAQADhFrz5etVRJp6hEmBr0SQo=").click()
            time.sleep(5)
            self.driver.find_element(By.CSS_SELECTOR,
                                     "#HubPersonaId_AAQkADc4YTU4NjRmLWJlZjUtNGE1Ny05ZTg1LTIyMDZlYmRmODcwNQAQADhFrz5etVRJp6hEmBr0SQo\\= .\\_23MAgMK72sYZSA6TScc0us").click()
            time.sleep(5)
            element = self.driver.find_element_by_xpath('//*[@id="a5nS-"]/section[1]/div[1]/div[1]/button/div/div')
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()

            element = self.driver.find_element_by_xpath('//*[@id="a5nS-"]/section[1]/div[1]/div[1]/div/span/i')
            hover = ActionChains(self.driver).move_to_element(element).click()
            hover.perform()
            click = self.driver.find_element_by_xpath('//*[@id="a5nS-"]/section[1]/div[1]/div[1]/div/span/i')
            click.click()
            s = pyperclip.paste()
            correos.append(s)
            # print(s)
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR,
                                     "#HubPersonaId_AAQkADc4YTU4NjRmLWJlZjUtNGE1Ny05ZTg1LTIyMDZlYmRmODcwNQAQAL4C7DJxhO1MqGJU\\+i\\+t7G8\\= .\\_23MAgMK72sYZSA6TScc0us").click()
            time.sleep(5)
            element = self.driver.find_element_by_xpath('//*[@id="a5nS-"]/section[1]/div[1]/div[1]/button/div/div')
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()

            element = self.driver.find_element_by_xpath('//*[@id="a5nS-"]/section[1]/div[1]/div[1]/div/span/i')
            hover = ActionChains(self.driver).move_to_element(element).click()
            hover.perform()
            click = self.driver.find_element_by_xpath('//*[@id="a5nS-"]/section[1]/div[1]/div[1]/div/span/i')
            click.click()
            s = pyperclip.paste()
            correos.append(s)

            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR,
                                     "#HubPersonaId_AAQkADc4YTU4NjRmLWJlZjUtNGE1Ny05ZTg1LTIyMDZlYmRmODcwNQAQAIrTnGf\\/\\+h5DqxNqiELcu\\+g\\= .\\_23MAgMK72sYZSA6TScc0us").click()
            time.sleep(5)
            element = self.driver.find_element_by_xpath('//*[@id="a5nS-"]/section[1]/div[1]/div[1]/button/div/div')
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()

            element = self.driver.find_element_by_xpath('//*[@id="a5nS-"]/section[1]/div[1]/div[1]/div/span/i')
            hover = ActionChains(self.driver).move_to_element(element).click()
            hover.perform()
            click = self.driver.find_element_by_xpath('//*[@id="a5nS-"]/section[1]/div[1]/div[1]/div/span/i')
            click.click()
            s = pyperclip.paste()
            correos.append(s)

            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR,
                                     "#HubPersonaId_AAQkADc4YTU4NjRmLWJlZjUtNGE1Ny05ZTg1LTIyMDZlYmRmODcwNQAQAIzeG8pRNrFPn\\/d\\+ot0MsFo\\= .\\_23MAgMK72sYZSA6TScc0us").click()
            time.sleep(5)
            element = self.driver.find_element_by_xpath('//*[@id="a5nS-"]/section[1]/div[1]/div[1]/button/div/div')
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()

            element = self.driver.find_element_by_xpath('//*[@id="a5nS-"]/section[1]/div[1]/div[1]/div/span/i')
            hover = ActionChains(self.driver).move_to_element(element).click()
            hover.perform()
            click = self.driver.find_element_by_xpath('//*[@id="a5nS-"]/section[1]/div[1]/div[1]/div/span/i')
            click.click()
            s = pyperclip.paste()
            correos.append(s)
            # self.driver.quit()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="O365_AppName"]/span').click()

            for i in correos:
                time.sleep(5)
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH,
                        '//*[@id="id__5"]'
                    ))).click()

                 # Establecemos el asunto
                time.sleep(10)
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH,
                        #"//*[@id='ReadingPaneContainerId']/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div"
                        #//*[@id="TextField1044"]
                        "//*[starts-with(@id, 'TextField')]"
                    )))
                element.send_keys("Correo del examen de simulación")

                # Establecemos el destinatario
                time.sleep(5)
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH,
                        '//*[@id="ReadingPaneContainerId"]/div/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div/div/input'
                    )))
                element.send_keys(i)

                # Seleccionamos el area de contenido del correo
                time.sleep(5)
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH,
                        "//*[@id='ReadingPaneContainerId']/div/div/div/div[1]/div[2]/div[1]"
                    ))).click()

                # Adjuntamos el flyer de Xavier Hervas
                time.sleep(5)
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.CSS_SELECTOR,
                        "#ReadingPaneContainerId > div > div > div > div._29NreFcQ3QoBPNO3rKXKB0 > div._1vGTUqFfb2m4yyZJJPHFDg._1PGX4GmfSf_CaaQSnoiB4l > input:nth-child(4)"
                    ))).send_keys('C:/Users/leand/Downloads/VOTA-12IDFlyer.png')

                # Damos click en el boton enviar
                time.sleep(15)
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH,
                        "//*[@id='ReadingPaneContainerId']/div/div/div/div[1]/div[3]/div[2]/div[1]/div/span/button[1]"
                    ))).click()

            with open("D:/Users/leand/PycharmProjects/EXAMEN/venv/bot/correos.txt", "w") as txt_file:
                for line in correos:
                    txt_file.write(" ".join(line) + "\n")
        except NoSuchElementException as e:
            self.ecepciones(e.msg)
        except Exception as e:
            self.ecepciones(e.args)
