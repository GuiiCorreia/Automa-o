from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class atividade():
    def __init__(self): #metodo construtor para iniciar o WebDriver
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get("https://seiteste.fiocruz.br/")
        self.browser.implicitly_wait(10)

    def __exit__(self, exc_type, exc_value, exc_tb): #metodo para fechar o programa
        if self.teardown:
            self.quit()

    def login(self): #poder fazer o login na pagina, colocando 'teste' como usuario e senha e posteriormente dar um click para executar o login 
        self.browser.find_element(By.XPATH,'//*[@id="txtUsuario"]').send_keys('teste')
        self.browser.find_element(By.XPATH,'//*[@id="pwdSenha"]').send_keys('teste')

        self.browser.find_element(By.XPATH,'//*[@id="chkLembrar"]').click()
        self.browser.find_element(By.XPATH,'//*[@id="sbmLogin"]').click()

    def processo(self): # metodo para poder fazer a busca do processo para ter acesso ao menu
        self.browser.find_element(By.XPATH,'//*[@id="txtPesquisaRapida"]').send_keys('92.000130/2020-12', Keys.ENTER)
        time.sleep(3)

    def menu(self, menu_option): # Metodo de Menu, onde de acordo com o texto de busca, ele vai executar um dos processos
        iframe = self.browser.find_element(By.ID, "ifrVisualizacao")
        self.browser.switch_to.frame(iframe)

        if menu_option == 'iniciar_processo': # Caso o texto por "iniciar_processo", ele vai executar a função de iniciar_processo()
                self.iniciar_processo()
        elif menu_option == 'consultar_processo': #Caso o texto por "consultar_processo", ele vai executar a função de consultar_processo()
                self.consultar_processo()
        elif menu_option == 'acompanhamento_especial': #Caso o texto por "acompanhamento_especial", ele vai executar a função de acompanhamento_especial()
                self.acompanhamento_especial()
        elif menu_option == 'anotacao': #Caso o texto por "anotacao", ele vai executar a função de anotacao()
                self.anotacao()
        elif menu_option == 'reabrir_processo':#Caso o texto por "reabrir_processo", ele vai executar a função de reabrir_processo()
                self.reabrir_processo()
        elif menu_option == 'gerar_pdf':#Caso o texto por "gerar_pdf", ele vai executar a função de gerar_pdf()
                self.gerar_pdf()
        elif menu_option == 'gerar_zip':#Caso o texto por "gerar_zip", ele vai executar a função de gerar_zip()
                self.gerar_zip()
        elif menu_option == 'ponto_controle':#Caso o texto por "ponto_controle", ele vai executar a função de ponto_controle()
                self.ponto_controle()
        elif menu_option == 'controle_processo':#Caso o texto por "controle_processo", ele vai executar a função de controle_processo()
                self.controle_processo()
        elif menu_option == 'pesquisar_processo':#Caso o texto por "pesquisar_processo", ele vai executar a função de pesquisar_processo()
                self.pesquisar_processo()
            


    def iniciar_processo(self): # metodo onde ele vai iniciar o processo para executar a função de iniciar os processos 
        button = self.browser.find_element(By.ID,'divArvoreAcoes')
        button.find_elements(By.TAG_NAME, 'a')[0].click()

    def consultar_processo(self): # metodo onde ele vai iniciar o processo para executar a função de consultar os processos
        button = self.browser.find_element(By.ID,'divArvoreAcoes')
        button.find_elements(By.TAG_NAME, 'a')[1].click()

    def acompanhamento_especial(self): # metodo onde ele vai iniciar o processo para executar a função de acompanhamento especial
        button = self.browser.find_element(By.ID,'divArvoreAcoes')
        button.find_elements(By.TAG_NAME, 'a')[2].click()

    def anotacao(self): # metodo onde ele vai iniciar o processo para executar a função de anotação
        button = self.browser.find_element(By.ID,'divArvoreAcoes')
        button.find_elements(By.TAG_NAME, 'a')[3].click()

    def reabrir_processo(self): # metodo onde ele vai iniciar o processo para executar a função de reabrir os processos
        button = self.browser.find_element(By.ID,'divArvoreAcoes')
        button.find_elements(By.TAG_NAME, 'a')[4].click()

    def gerar_pdf(self):# metodo onde ele vai iniciar o processo para executar a função de gerar pdf
        button = self.browser.find_element(By.ID,'divArvoreAcoes')
        button.find_elements(By.TAG_NAME, 'a')[5].click()

    def gerar_zip(self): # metodo onde ele vai iniciar o processo para executar a função de gerar zip
        button = self.browser.find_element(By.ID,'divArvoreAcoes')
        button.find_elements(By.TAG_NAME, 'a')[6].click()

    def ponto_controle(self): # metodo onde ele vai iniciar o processo para executar a função de ponto de controle
        button = self.browser.find_element(By.ID,'divArvoreAcoes')
        button.find_elements(By.TAG_NAME, 'a')[7].click()

    def controle_processo(self): # metodo onde ele vai iniciar o processo para executar a função de controle de processos 
        button = self.browser.find_element(By.ID,'divArvoreAcoes')
        button.find_elements(By.TAG_NAME, 'a')[8].click()

    def pesquisar_processo(self): # metodo onde ele vai iniciar o processo para executar a função de pesquisar processos
        button = self.browser.find_element(By.ID,'divArvoreAcoes')
        button.find_elements(By.TAG_NAME, 'a')[9].click()

iniciar = atividade() #definir a variavel para iniciar o bot
iniciar.login()#executar o metodo para fazer login 
iniciar.processo()#executar o metodo de iniciar os processos
iniciar.menu('gerar_pdf')#executar o metodo de menu, colocando o texto desejado nas aspas






        