from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.deliverinhour.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='pull-right']//a[@class='index-footer btn btn-md waves-effect waves-light'][normalize-space()='Login']").click()
time.sleep(2)
driver.find_element(By.ID, "email").send_keys("sandesh@acceinfo.com")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("Testing@123456")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='remember']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='SIGN IN']").click()
time.sleep(2)
driver.find_element(By.XPATH, " //a[normalize-space()='New Request']").click()
time.sleep(2)
driver.find_element(By.XPATH, " //button[normalize-space()='More Details']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='d_email']").send_keys("sandesh@acceinfo.com")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='d_from_add']").send_keys("210 cabin trail stouffville")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='d_to_add']").send_keys("141-200 veterans drive brampton")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@id='submit_direct']").click()
time.sleep(4)
