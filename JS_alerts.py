import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[contains(text(),'JS')]").click()
time.sleep(3)
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
driver.find_element(By.XPATH,"//button[contains(text(),'Confirm')]").click()
time.sleep(4)
alert2=driver.switch_to.alert
print(alert2.text)
alert2.dismiss()
time.sleep(3)
driver.find_element(By.XPATH,"//button[contains(text(),'Prompt')]").click()
time.sleep(4)
alert3=driver.switch_to.alert
print(alert3.text)
alert3.send_keys("Kishore")
time.sleep(3)
alert3.accept()
result_text = driver.find_element(By.ID, "result").text
clean_text = result_text.replace("You entered:", "").strip()
print("Result displayed on page:", clean_text)

time.sleep(3)