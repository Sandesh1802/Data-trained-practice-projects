from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

signin = driver.get("https://www.saucedemo.com/")
driver.maximize_window()
username = driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
password = driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
signin = driver.find_element(By.ID, "login-button").click()
time.sleep(2)
DD = driver.find_element(By.CLASS_NAME, "product_sort_container")
dropdown = Select(DD)
time.sleep(2)
dropdown.select_by_visible_text("Name (Z to A)")
time.sleep(5)
option = driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(2)
closebutton = driver.find_element(By.ID, "react-burger-cross-btn").click()
time.sleep(2)
DD = driver.find_element(By.CLASS_NAME, "product_sort_container")
dropdown = Select(DD)
time.sleep(2)
dropdown.select_by_visible_text("Name (A to Z)")
time.sleep(2)
addtocart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(2)
remove = driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
time.sleep(2)
add_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
add_button.screenshot(".\\add_test.png")
time.sleep(2)
driver.get_screenshot_as_file("C:\\Users\Anjana Sandesh\PycharmProjects\AutomationSelenium\Learning python\\add_btn_test.png")
time.sleep(2)
option = driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(2)
logout = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
driver.close()






