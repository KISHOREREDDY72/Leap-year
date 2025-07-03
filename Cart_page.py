import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(8)
driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("ca")
time.sleep(3)
cart=driver.find_elements(By.XPATH,"//button[contains(text(),'ADD TO CART')]")
for clicks in cart:
    clicks.click()
time.sleep(4)
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,".promocode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
time.sleep(2)
dropdown=Select(driver.find_element(By.XPATH,"//select"))
dropdown.select_by_visible_text("India")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[text()='Proceed']").click()
time.sleep(5)

