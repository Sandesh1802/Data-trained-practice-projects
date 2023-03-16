from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

service_obj = Service("C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("ber")
driver.find_element(By.CLASS_NAME,"search-button").click()

driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]").click()
driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]").click()
driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[1]/div[3]/div[3]/button[1]").click()

