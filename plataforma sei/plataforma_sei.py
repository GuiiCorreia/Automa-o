from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time 

class SEI():
    def __init__(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get("https://sipseiteste.fiocruz.br/login.php?sigla_orgao_sistema=FIOCRUZ&sigla_sistema=SEI")
        self.browser.implicitly_wait(10)

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.teardown:
            self.quit()
    
    def teste_login(self):
        login = self.browser.find_element(By.XPATH,'//*[@id="txtUsuario"]').send_keys('teste')
        senha = self.browser.find_element(By.XPATH,'//*[@id="pwdSenha"]').send_keys('teste')

        lembrar_senha = self.browser.find_element(By.XPATH,'//*[@id="chkLembrar"]').click()
        button = self.browser.find_element(By.XPATH,'//*[@id="sbmLogin"]').click()

    def pesquisa(self):
        pesquisa = self.browser.find_element(By.XPATH,'//*[@id="txtPesquisaRapida"]').send_keys('92.000114/2020-20', Keys.ENTER)
        time.sleep(3)

    def colocar_documento(self):
        iframe = self.browser.find_element(By.ID, "ifrVisualizacao")
        self.browser.switch_to.frame(iframe)
        incluir_documento = self.browser.find_element(By.XPATH, "//*[@id='divArvoreAcoes']/a[1]/img").click()
        button_externo = self.browser.find_element(By.XPATH,'//*[@id="tblSeries"]/tbody/tr[1]/td/a[2]').click()
        button_anexo = self.browser.find_element(By.XPATH,'//*[@id="selSerie"]/option[12]').click()
        button_data = self.browser.find_element(By.XPATH,'//*[@id="txtDataElaboracao"]').send_keys('26/05/2022')
        button_formato = self.browser.find_element(By.XPATH,'//*[@id="optNato"]').click()
        button_acesso = self.browser.find_element(By.XPATH,'//*[@id="optPublico"]').click()

        enviar_arquivo = self.browser.find_element(By.XPATH,'//*[@id="filArquivo"]').send_keys('C:\\Users\\Guilherme\\Documents\\Faculdade\\Jesmmer\\booking\\Atv1 - Guilherme Correia.pdf')
        time.sleep(3)
        enviar = self.browser.find_element(By.XPATH,'//*[@id="btnSalvar"]').click()
        



iniciar = SEI()
iniciar.teste_login()
iniciar.pesquisa()
iniciar.colocar_documento()