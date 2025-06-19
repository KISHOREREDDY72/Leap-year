import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import date, timedelta


driver=webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
driver.maximize_window()
print(driver.current_url)
#name=driver.find_element(By.XPATH, "//input[@class='form-control ng-pristine ng-invalid ng-touched' and @name='name']")
locator_path = "(//input[@name='name'])[1]"
driver.find_element(By.XPATH, locator_path).send_keys("Hello Automation")
driver.find_element(
    By.NAME,"email"
).send_keys("xyz@gmail.com")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("123456789")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
dropdown = driver.find_element(By.ID, "exampleFormControlSelect1")
s1 = Select(dropdown)
s1.select_by_visible_text("Female")
driver.find_element(By.ID,"inlineRadio1").click()
tomorrow = date.today() + timedelta(days=2)
formatted_date = tomorrow.strftime("%Y-%m-%d")
date_input = driver.find_element(By.NAME, "bday")
date_input.send_keys(formatted_date)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
success_alert = WebDriverWait(driver, 10).until(
    expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-success"))
)
assert "Success! The Form has been submitted successfully!" in success_alert.text
print("Assertion is Successful")



time.sleep(
    4
)

driver.quit()


