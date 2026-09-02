import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MultipleElementsDemo:
    def __init__(self, target_url):
        self.driver = webdriver.Chrome()
        self.url = target_url
        self.wait = WebDriverWait(self.driver, 10)

    def demonstrate_multiple_elements(self):
        try:
            print("Navigating to target webpage...")
            self.driver.get(self.url)
            self.driver.maximize_window()

            # Wait for the page body to be fully loaded before interacting
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            # 1. Working with multiple interactive elements (Checkboxes)
            print("1. Locating multiple checkbox elements...")
            # Use find_elements (plural) to get a list of all checkboxes
            checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
            print(f" -> Found {len(checkboxes)} checkboxes. Clicking all of them...")
            
            for index, checkbox in enumerate(checkboxes):
                checkbox.click()
                # Assert to verify each checkbox in the list was actually selected
                assert checkbox.is_selected(), f"Checkbox {index + 1} failed to select."
            print(" -> Success: All checkboxes successfully located, clicked, and verified.")

            # 2. Extracting text from multiple elements (Links)
            print("\n2. Locating all hyperlink (<a>) elements on the page...")
            links = self.driver.find_elements(By.TAG_NAME, "a")
            
            # Assert to verify the list of links is not empty
            assert len(links) > 0, "Failed: No links found on the page."
            print(f" -> Success: Found {len(links)} total links on the page.")
            
            print(" -> Extracting and printing text for the first 10 visible links:")
            visible_count = 0
            for link in links:
                text = link.text.strip()
                # Filter out empty or hidden links
                if text:
                    print(f"    - {text}")
                    visible_count += 1
                if visible_count == 10:
                    break

            print("\nAll multiple element operations successfully executed and asserted.")
            
            # Pause briefly so the final results can be seen in the video recording
            time.sleep(3)

        finally:
            print("Demonstration complete. Closing browser...")
            self.driver.quit()

if __name__ == "__main__":
    demo = MultipleElementsDemo("https://rahulshettyacademy.com/AutomationPractice/")
    demo.demonstrate_multiple_elements()