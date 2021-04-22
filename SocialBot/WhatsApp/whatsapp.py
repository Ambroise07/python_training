#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import sys

class WhatsApp :
    "La class du bot whatsapp "
    def connect(self) :

        self.driver = webdriver.Firefox()
        self.driver.get("https://web.whatsapp.com/")
        input('Taper Entrer après le scannage du code Qr')
        
        self.driver.implicitly_wait(10)
        time.sleep(10.1)
        try :
            self.attente = WebDriverWait(driver, 10)
            self.element = self.attente.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[1]/div/button')))
        except :
            time.sleep(10.10)
            print('chargement complet de la page en cours ')
        print("Vous êtes connecté !")

    def SendMessage(self) :

        def Contact() :#SearchContact.send_keys(contact)
            XpathS = "//input[@title='Rechercher ou démarrer une nouvelle discussion']"
            contact = input('Enter le nom de votre contact __-> ')
            print("Tentatif de recherche de votre contact")
            self.driver.implicitly_wait(5)
            SearchContact = self.driver.find_element_by_xpath(XpathS)
            SearchContact.click()
            self.driver.implicitly_wait(30)
            print('typologie')
            SearchContact.send_keys(Keys.CONTROL + contact)
        Contact()

    def personal_Message(self) :

            driver = self.driver
            
            Message = "c'est gratuit chef  !"
            try:
                attente = WebDriverWait(driver, 125)
                self.element = attente.until(EC.element_to_be_clickable((By.XPATH, '//span[@title = "{}"]'.format('Rostant'))))
            except Exception :
                print("Domm1 !")

            dest = driver.find_element_by_xpath('//span[@title = "{}"]'.format('Rostant')) #Le Destinatair du Message 
            dest.click()
            Message_input = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
            Message_input.send_keys(Message)
            try:
                elem = WebDriverWait(driver, 125)
                self.poil = attente.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')))
            except Exception :
                print("Domm2 !")
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button').click()





    def disconnect(self) :

        driver = self.driver
        driver.close()

bot = WhatsApp()
bot.SendMessage()

"""contact = input("Enter le nom ")
text = input("Entrer le message !")
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")
inp_xpath_search = "//input[@title='Rechercher ou démarrer une nouvelle discussion']"
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()
inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
input_box.send_keys(text + Keys.ENTER)
time.sleep(2)"""