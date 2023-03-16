from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

signin = driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
time.sleep(2)
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
drag = driver.find_element(By.ID, "draggable")
drop = driver.find_element(By.ID, "droppable")

ActionChains(driver).drag_and_drop( driver.find_element(By.ID, "draggable"), driver.find_element(By.ID, "droppable")).perform()
time.sleep(2)

#Another way of doing it

ActionChains(driver).drag_and_drop(drag , drop).perform()
time.sleep(2)


ActionChains(driver).drag_and_drop(drag, drop).perform()
time.sleep(2)
time.sleep(3)
driver.close()