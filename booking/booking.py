from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time 

class booking():
    def __init__(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get("https://www.booking.com/")
        self.browser.implicitly_wait(10)

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.teardown:
            self.quit()
    
    def moeda(self, currency):
        button = self.browser.find_element(By.CSS_SELECTOR,'[data-tooltip-text="Escolha sua moeda"]').click()
        moeda = self.browser.find_element(By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]').click()

    def local(self, place_to_go):
        limpar = self.browser.find_element(By.XPATH,'//*[@id="ss"]').clear()
        local = self.browser.find_element(By.XPATH,'//*[@id="ss"]').send_keys(place_to_go)
        resultado = self.browser.find_element(By.CSS_SELECTOR,'li[data-i="0"]').click()

    def datas(self, check_in_date, check_out_date):
        ida = self.browser.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]').click()
        volta = self.browser.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]').click()
        
    def hospedagem(self, adultos = 3, criancas = 2):
        pessoas = self.browser.find_element(By.ID, 'xp__guests__toggle').click()

        #adultos
        adulto = self.browser.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div[2]/span[1]')
        diminuir_adulto = self.browser.find_element(By.XPATH,'//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div[2]/button[1]')
        aumentar_adulto = self.browser.find_element(By.XPATH,'//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div[2]/button[2]')

        while True:
            if int(adulto.text) > adultos:
                diminuir_adulto.click()
            elif int(adulto.text) < adultos:
                aumentar_adulto.click()
            else:
                break
        
        #crianças
        crianca = self.browser.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[2]/div/div[2]/span[1]')
        diminuir_crianca = self.browser.find_element(By.XPATH,'//*[@id="xp__guests__inputs-container"]/div/div/div[2]/div/div[2]/button[1]')
        aumentar_crianca = self.browser.find_element(By.XPATH,'//*[@id="xp__guests__inputs-container"]/div/div/div[2]/div/div[2]/button[2]')

        while True:
            if int(crianca.text) > criancas:
                diminuir_crianca.click()
            elif int(crianca.text) < criancas:
                aumentar_crianca.click()
            else:
                break
        
        if criancas > 0:
            for i in range(1,criancas+1):
                button = Select(self.browser.find_element(By.XPATH,f'//*[@id="xp__guests__inputs-container"]/div/div/div[3]/select[{i}]'))
                button.select_by_value('5')

        quartos = self.browser.find_element(By.CSS_SELECTOR, '[aria-label="Aumentar número de Quartos"]').click()
        
        self.browser.find_element(By.XPATH, '//*[@id="frm"]/div[1]/div[4]/div[2]/button').click()


iniciar = booking()
iniciar.moeda(currency='BRL')
iniciar.local('Rio de Janeiro')
iniciar.datas(check_in_date='2022-10-16', check_out_date='2022-10-23')
iniciar.hospedagem(2, 3)



    


