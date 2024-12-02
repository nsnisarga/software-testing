# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Replace these with your GitHub credentials and repository details
# GITHUB_USERNAME = "nisarganayak02@gmail.com"
# GITHUB_PASSWORD = "Nisarga@19112002"
# REPO_NAME = "demo"  # Repository name is now fixed as "demo"
# REPO_DESCRIPTION = "This is an automated repository created using Selenium."

# class GitHubAutomation:
#     def __init__(self):
#         # Initialize the WebDriver
#         self.driver = webdriver.Chrome()  # Or use webdriver.Firefox(), etc., based on your browser
#         self.wait = WebDriverWait(self.driver, 10)

#     def login(self):
#         try:
#             # Open GitHub login page
#             self.driver.get("https://github.com/login")

#             # Enter username
#             username_field = self.wait.until(EC.presence_of_element_located((By.ID, "login_field")))
#             username_field.send_keys(GITHUB_USERNAME)

#             # Enter password
#             password_field = self.driver.find_element(By.ID, "password")
#             password_field.send_keys(GITHUB_PASSWORD)

#             # Click on login button
#             login_button = self.driver.find_element(By.NAME, "commit")
#             login_button.click()

#             print("Login successful!")

#         except Exception as e:
#             print(f"Login failed: {e}")

#     def create_repository(self):
#         try:
#             # Navigate to "New repository" page
#             self.driver.get("https://github.com/new")

#             # Enter repository name (fixed as "demo")
#             repo_name_field = self.wait.until(EC.presence_of_element_located((By.ID, ":r5:")))  # Updated ID for repository name
#             repo_name_field.send_keys(REPO_NAME)

#             # Enter repository description (optional)
#             description_field = self.driver.find_element(By.ID, ":ra:")  # Updated ID for description field
#             description_field.send_keys(REPO_DESCRIPTION)

#             # Check "Initialize this repository with a README" (optional)
#             init_readme_checkbox = self.driver.find_element(By.ID, "repository_auto_init")
#             if not init_readme_checkbox.is_selected():
#                 init_readme_checkbox.click()

#             # Immediately click "Create repository" after entering description
#             create_button = self.driver.find_element(By.CSS_SELECTOR, "button.Box-sc-g0xbh4-0.jLvIcQ.prc-Button-ButtonBase-c50BI")
#             create_button.click()

#             print(f"Repository '{REPO_NAME}' created successfully!")

#         except Exception as e:
#             print(f"An error occurred while creating the repository: {e}")

#     def close(self):
#         # Close the browser
#         time.sleep(5)  # Optional: Wait for 5 seconds before closing
#         self.driver.quit()

# if __name__ == "__main__":
#     # Create an instance of the automation class with the fixed repository name
#     github_automation = GitHubAutomation()

#     # Log in to GitHub
#     github_automation.login()

#     # Create a new repository
#     github_automation.create_repository()

#     # Close the browser after the task is completed
#     github_automation.close()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace these with your GitHub credentials and repository details
GITHUB_USERNAME = "nisarganayak02@gmail.com"
GITHUB_PASSWORD = "Nisarga@19112002"
REPO_NAME = "demo"  # Repository name is now fixed as "demo"
REPO_DESCRIPTION = "This is an automated repository created using Selenium."

class GitHubAutomation:
    def __init__(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome()  # Or use webdriver.Firefox(), etc., based on your browser
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        try:
            # Open GitHub login page
            self.driver.get("https://github.com/login")

            # Enter username
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "login_field")))
            username_field.send_keys(GITHUB_USERNAME)

            # Enter password
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys(GITHUB_PASSWORD)

            # Click on login button
            login_button = self.driver.find_element(By.NAME, "commit")
            login_button.click()

            print("Login successful!")

        except Exception as e:
            print(f"Login failed: {e}")

    def create_repository(self):
        try:
            # Navigate to "New repository" page
            self.driver.get("https://github.com/new")

            # Enter repository name (fixed as "demo")
            repo_name_field = self.wait.until(EC.presence_of_element_located((By.ID, ":r5:")))  # Updated ID for repository name
            repo_name_field.send_keys(REPO_NAME)

            # Enter repository description (optional)
            description_field = self.driver.find_element(By.ID, ":ra:")  # Updated ID for description field
            description_field.send_keys(REPO_DESCRIPTION)

            # Check "Initialize this repository with a README" (optional)
            init_readme_checkbox = self.driver.find_element(By.ID, "repository_auto_init")
            if not init_readme_checkbox.is_selected():
                init_readme_checkbox.click()

            # Immediately click "Create repository" after entering description
            create_button = self.driver.find_element(By.CSS_SELECTOR, "button.Box-sc-g0xbh4-0.jLvIcQ.prc-Button-ButtonBase-c50BI")
            create_button.click()

            print(f"Repository '{REPO_NAME}' created successfully!")

        except Exception as e:
            print(f"An error occurred while creating the repository: {e}")

    def close(self):
        # Close the browser
        time.sleep(5)  # Optional: Wait for 5 seconds before closing
        self.driver.quit()

if __name__ == "__main__":
    # Create an instance of the automation class with the fixed repository name
    github_automation = GitHubAutomation()

    # Log in to GitHub
    github_automation.login()

    # Create a new repository
    github_automation.create_repository()

    # Close the browser after the task is completed
    github_automation.close()
