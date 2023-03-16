from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.yatra.com/")

depart_from = driver.find_element(By.ID, "BE_flight_origin_city")
depart_from.click()
time.sleep(4)
depart_from.send_keys("Toronto")
time.sleep(2)
depart_from.send_keys(Keys.ENTER)
time.sleep(2)
going_to = driver.find_element(By.XPATH, " //input[@id='BE_flight_arrival_city']")
going_to.send_keys("New")
time.sleep(2)
search_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
for results in search_result:
    print(results.text)
    if "NEW BERN (EWN)" in results.text:
        results.click()
        time.sleep(4)
        break



