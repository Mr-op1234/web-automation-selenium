import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CSSWildcardDemo:
    def __init__(self, target_url):
        self.driver = webdriver.Chrome()
        self.url = target_url
        self.wait = WebDriverWait(self.driver, 10)

    def demonstrate_wildcards(self):
        try:
            print("Navigating to target webpage...")
            self.driver.get(self.url)
            self.driver.maximize_window()

            # 1. Prefix Match (^=) -> Matches attributes STARTING with a value
            print("1. Locating element with prefix '^='...")
            prefix_element = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id^='checkBoxOption']"))
            )
            prefix_element.click()
            # Assert to verify the checkbox was actually selected
            assert prefix_element.is_selected(), "Prefix wildcard failed: Checkbox is not selected."
            print(" -> Success: Prefix element located and verified.")

            # 2. Suffix Match ($=) -> Matches attributes ENDING with a value
            print("2. Locating element with suffix '$='...")
            suffix_element = self.driver.find_element(By.CSS_SELECTOR, "input[value$='2']")
            suffix_element.click()
            # Assert to verify the radio button was actually selected
            assert suffix_element.is_selected(), "Suffix wildcard failed: Radio button is not selected."
            print(" -> Success: Suffix element located and verified.")

            # 3. Substring Match (*=) -> Matches attributes CONTAINING a value
            print("3. Locating element with substring '*='...")
            substring_element = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder*='Select Countries']")
            substring_element.send_keys("India")
            # Assert to verify the text was actually entered into the field
            assert substring_element.get_attribute("value") == "India", "Substring wildcard failed: Text not entered."
            print(" -> Success: Substring element located and verified.")
            
            print("\nAll dynamic elements successfully located and asserted using CSS wildcards.")
            
            # Pause briefly so the final results can be seen in the video recording
            time.sleep(3)

        finally:
            print("Demonstration complete. Closing browser...")
            self.driver.quit()

if __name__ == "__main__":
    demo = CSSWildcardDemo("https://rahulshettyacademy.com/AutomationPractice/")
    demo.demonstrate_wildcards()