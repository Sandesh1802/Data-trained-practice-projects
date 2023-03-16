from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.salesforce.com/ca/form/signup/freetrial-elf-v2/?nc=7010M000000uBptQAE&d=glob-nav-2")

DD = driver.find_element(By.NAME, "CompanyCountry")
dropdown = Select(DD)

dropdown.select_by_visible_text("Cambodia")
time.sleep(2)
dropdown.select_by_value("US")
time.sleep(2)
dropdown.select_by_value("CA")
time.sleep(2)
dropdown.select_by_index(15)
time.sleep(2)



