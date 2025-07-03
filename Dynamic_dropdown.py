import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID,"autosuggest").send_keys("uni")
# united_states_option = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.XPATH, suggestion_xpath))
# )
suggestion_xpath = "//li[@class='ui-menu-item']/a[contains(text(), 'United States')]"
united_states_option = driver.find_element(By.XPATH,suggestion_xpath)

united_states_option.click()
time.sleep(4)


