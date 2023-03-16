from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://automate-apps.com/select-multiple-options-from-a-drop-down-list/")

DD = driver.find_element(By.NAME, "cars")
dropdown = Select(DD)

dropdown.select_by_visible_text("Maruti")
time.sleep(2)
dropdown.select_by_value("B")
time.sleep(2)
dropdown.select_by_index(3)
time.sleep(2)
dropdown.deselect_by_value("M")
time.sleep(2)
dropdown.deselect_all()
time.sleep(2)
