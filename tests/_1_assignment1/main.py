from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver, 10)

    # 1. By.ID -> Username field by ID
    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    print(f"[By.ID] Found: {username_field.get_attribute('id')}")
    username_field.send_keys("tomsmith")

    # 2. By.NAME -> Password field by Name
    password_field = driver.find_element(By.NAME, "password")
    print(f"[By.NAME] Found: {password_field.get_attribute('name')}")
    password_field.send_keys("SuperSecretPassword!")

    # 3. By.CLASS_NAME -> Button by Class Name
    login_button = driver.find_element(By.CLASS_NAME, "radius")
    print(f"[By.CLASS_NAME] Found: {login_button.text}")

    # 4. By.TAG_NAME -> Header by Tag Name
    header = driver.find_element(By.TAG_NAME, "h2")
    print(f"[By.TAG_NAME] Found h2: {header.text}")

    # 5. By.LINK_TEXT -> Link by exact Link Text
    link = driver.find_element(By.LINK_TEXT, "Elemental Selenium")
    print(f"[By.LINK_TEXT] Found link: {link.text}")

    print("\nAll 5 locators worked!")

finally:
    time.sleep(3)
    driver.quit()