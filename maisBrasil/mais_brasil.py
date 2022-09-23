from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import openpyxl
import time

class mais_brasil:  

    def iniciar_bot(self):
        self.iniciar_webdriver()
        self.pesquisar_informacoes()
        self.dados_planilha()
        self.pegar_cnpj()

    def iniciar_webdriver(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument('--disable-notifications')
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get("https://voluntarias.plataformamaisbrasil.gov.br/voluntarias/Principal/Principal.do?Usr=guest&Pwd=guest")
        self.browser.implicitly_wait(10)
        time.sleep(2)

    def pesquisar_informacoes(self):
        botao_convenios = self.browser.find_element(By.XPATH, '//*[@id="menuPrincipal"]/div[1]/div[4]').click()
        botao_consultar = self.browser.find_element(By.XPATH, '//*[@id="contentMenu"]/div/ul/li/a').click()

        
    def dados_planilha(self):
        df = pd.read_excel('C:\\Users\\Guilherme\\Documents\\Faculdade\\Jesmmer\\maisBrasil\\solicitacoes.xlsx', engine='openpyxl') #, usecols='A' #alterar o local onde a planilha esta
        dados = []
        colunas = ["N° Convênio", "CNPJ"]
        cont = 0
        for ind, linha in df.iterrows():
            convenio = int(linha.iloc[0])
            cnpj = self.pegar_cnpj(convenio)
            dados += [[convenio, cnpj]]
            if cont == 10:
                break
            cont+=1

        df = pd.DataFrame(dados, columns=colunas)
        df.to_excel('cnpj.xlsx', index=False)
        self.close()

    def pegar_cnpj(self, convenio):
        bt_execucao = self.browser.find_element(By.CSS_SELECTOR,'div[href="#CONVENIOS"]').click()
        bt_consultar = self.browser.find_element(By.LINK_TEXT,"Consultar Convênios/Pré-Convênios").click()
        consulta = self.browser.find_element(By.ID,"consultarNumeroConvenio").send_keys(convenio)
        bt_consultar = self.browser.find_element(By.XPATH,'//*[@id="form_submit"]').click()
        tabela = self.browser.find_element(By.CSS_SELECTOR,"div[class='numeroConvenio']")
        link = tabela.find_element(By.TAG_NAME,'a').click()
        
        cnpj = self.browser.find_element(By.XPATH, "//tr[@class='proponente']/td[@class='field']").text
        return cnpj
    

iniciar = mais_brasil()
iniciar.iniciar_bot()
