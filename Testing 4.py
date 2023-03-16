from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.yatra.com/offer/dom/listing/domestic-flight-deals")

great_button = driver.find_element(By.XPATH, "//h2[normalize-space()='Great Offers & Amazing Deals']")
great_button.screenshot(".\\great_test.png")
time.sleep(2)
driver.get_screenshot_as_file("C:\\Users\Anjana Sandesh\PycharmProjects\AutomationSelenium\Learning python\\great_btn_test2.png")
time.sleep(2)

