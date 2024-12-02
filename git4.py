from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace these with your GitHub credentials
GITHUB_USERNAME = "nisarganayak02@gmail.com"
GITHUB_PASSWORD = "Nisarga@19112002"
REPO_NAME = "demo"
REPO_DESCRIPTION = "This is an automated repository created using Selenium."

class GitHubAutomation:
    def __init__(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome()  # Use the appropriate driver (e.g., webdriver.Firefox())
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        try:
            # Open GitHub login page
            self.driver.get("https://github.com/login")
            time.sleep(2)  # Wait for the page to load

            # Enter username
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "login_field")))
            username_field.send_keys(GITHUB_USERNAME)
            time.sleep(3)

            # Enter password
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys(GITHUB_PASSWORD)
            time.sleep(3)

            # Click on the login button
            login_button = self.driver.find_element(By.NAME, "commit")
            login_button.click()
            time.sleep(3)

            print("Login successful!")

        except Exception as e:
            print(f"Login failed: {e}")

    def create_repository(self):
        try:
            # Navigate to "New repository" page
            self.driver.get("https://github.com/new")
            time.sleep(3)

            # Enter repository name
            repo_name_field = self.wait.until(EC.presence_of_element_located((By.ID, ":r5:")))
            repo_name_field.send_keys(REPO_NAME)
            time.sleep(3)

            # Enter repository description (optional)
            description_field = self.wait.until(EC.presence_of_element_located((By.ID, ":ra:")))
            description_field.send_keys(REPO_DESCRIPTION)
            time.sleep(3)

            # Select "Private" radio button
            private_radio = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.Radio__StyledRadio-sc-1tx0ht9-0[value='private']")))
            private_radio.click()
            time.sleep(3)
            print("Private repository option selected successfully!")

            # Check "Initialize this repository with a README"
            try:
                init_readme_checkbox = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input.Checkbox__StyledCheckbox-sc-1ga3qj3-0[aria-describedby$='-caption']"))
                )
                if not init_readme_checkbox.is_selected():
                    init_readme_checkbox.click()
                time.sleep(3)
                print("Initialized repository with a README.")
            except Exception as e:
                print(f"Failed to initialize README: {e}")

            # Click "Create repository" button
            create_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'][aria-describedby*='-loading-announcement']"))
            )
            create_button.click()
            time.sleep(2)

            print(f"Repository '{REPO_NAME}' created successfully!")

        except Exception as e:
            print(f"An error occurred while creating the repository: {e}")

    def close(self):
        # Close the browser
        time.sleep(5)  # Optional: Wait for 5 seconds before closing
        self.driver.quit()

if __name__ == "__main__":
    # Create an instance of the automation class
    github_automation = GitHubAutomation()

    # Log in to GitHub
    github_automation.login()

    # Create a new repository
    github_automation.create_repository()

    # Close the browser after the task is completed
    github_automation.close()
