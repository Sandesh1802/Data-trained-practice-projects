from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

service_obj = Service("C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://canadianallcare.com/")
driver.maximize_window()

driver.find_element(By.NAME,"firstname").send_keys("sandesh")
driver.find_element(By.NAME,"lastname").send_keys("mokshaprasad")
driver.find_element(By.NAME,"campus-location").send_keys("stouffville")
driver.find_element(By.NAME,"phone").send_keys("9886535476")
driver.find_element(By.NAME,"your-email").send_keys("sandeshmoksh18@gmail.com")
driver.find_element(By.NAME,"your-message").send_keys("selenium is easy to learn")


