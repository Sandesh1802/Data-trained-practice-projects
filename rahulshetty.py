from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

service_obj = Service("C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.NAME,"name").send_keys("sandesh")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("abc123")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.NAME,"email").send_keys("sandeshmoksh18@gmail.com")

gender = Select(driver.find_element(By.ID,'exampleFormControlSelect1'))
gender.select_by_visible_text("Female")
gender.select_by_index(0)

#radiobutton
driver.find_element(By.XPATH,"//input[@value='option1']").click()
driver.find_element(By.XPATH,"//input[@id='inlineRadio2']").click()
driver.find_element(By.XPATH,"//input[@value='Submit']").click()

#practice
a=10
b=5
if a>b:
    print("a is greater than b")


