from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

# Child selectors — all scoped to the #login form
username_field = driver.find_element(By.CSS_SELECTOR, "#login input[name='username']")
password_field = driver.find_element(By.CSS_SELECTOR, "#login input[name='password']")
login_button   = driver.find_element(By.CSS_SELECTOR, "#login > button")

username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")
login_button.click()

time.sleep(1)
print(driver.find_element(By.CSS_SELECTOR, "#flash").text)

driver.quit()