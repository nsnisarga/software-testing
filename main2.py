import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class WhatsAppWebLoginTest(unittest.TestCase):
    
    def setUp(self):
        # Set up the WebDriver (ensure you have the appropriate driver installed)
        chrome_driver_path = "path/to/chromedriver"  # Replace with the actual path
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://web.whatsapp.com/")
        self.driver.maximize_window()
    
    def test_login_whatsapp(self):
        driver = self.driver
        
        print("Please scan the QR code to log in.")
        # Wait for user to scan the QR code (adjust time if necessary)
        time.sleep(20)  # Ensure you give sufficient time for login
        
        try:
            # Check if the main WhatsApp Web interface is loaded
            search_box = driver.find_element(By.XPATH, '//div[@title="Search input textbox"]')
            if search_box:
                print("Login successful! You can now use WhatsApp Web.")
        except Exception as e:
            print("Login failed or took too long. Please try again.")
            print(f"Error: {e}")
    
    def tearDown(self):
        # Quit the WebDriver session
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
