from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GitHubLoginTest:
    def setUp(self):
        
        self.driver = webdriver.Chrome()  
        self.driver.get("https://github.com/login")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver

        
        username = "nisarganayak02@gmail.com"
        password = "Nisarga@19112002"

        try:
            
            username_field = driver.find_element(By.ID, "login_field")
            username_field.clear()
            username_field.send_keys(username)

            
            password_field = driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(password)

            
            driver.find_element(By.NAME, "commit").click()

        
            time.sleep(5)

            
            profile_icon = driver.find_element(By.XPATH, "//summary[@aria-label='View profile and more']")
            print("Login successful! Profile icon found.")
        except Exception as e:
            print(f"Login failed: {e}")
        
        
        time.sleep(25)

    def tearDown(self):
        
        self.driver.quit()

if __name__ == "__main__":
    test = GitHubLoginTest()
    test.setUp()
    test.test_login()
    test.tearDown()
