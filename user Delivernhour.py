from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

signin = driver.get("https://www.deliverinhour.com/signin")
time.sleep(2)
register = driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
time.sleep(2)
FirstName = driver.find_element(By.XPATH, "//input[@id='fname']").send_keys("chaithanya")
time.sleep(2)
LastName = driver.find_element(By.XPATH, "//input[@id='lname']").send_keys("Raj")
time.sleep(2)
Email = driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Testing2@gmail.com")
time.sleep(2)
contactno = driver.find_element(By.XPATH, "//input[@id='mobile']").send_keys("4372555961")
time.sleep(2)
Otp = driver.find_element(By.NAME, "sendotp").click()
time.sleep(2)




