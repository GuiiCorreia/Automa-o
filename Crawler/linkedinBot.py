from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.linkedin.com/login")

input_email = browser.find_element_by_id("username")
input_email.send_keys('ca2277283@gmail.com')

input_senha = browser.find_element_by_id("password")
input_senha.send_keys('Smartleads1')
btn_login = browser.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button")
btn_login.click()

busca = browser.find_element_by_xpath("//*[@id='global-nav-search']/div/button")
time.sleep(3)
busca.send_keys('Python')
busca.send_keys(Keys.ENTER)

time.sleep(3)

filtro_vagas = browser.find_element_by_xpath("//button[@aria-label='Vagas']")
filtro_vagas.click()

input('')