from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

service_obj = Service("C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://login.salesforce.com/?locale=ca")
driver.maximize_window()

driver.find_element(By.NAME,"username").send_keys("anjana")
driver.find_element(By.ID,"password").send_keys("abc123")

