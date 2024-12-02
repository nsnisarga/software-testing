from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace these with your GitHub credentials and repository details
GITHUB_USERNAME = "nisarganayak02@gmail.com"
GITHUB_PASSWORD = "Nisarga@19112002"
REPO_NAME = "demo"
REPO_DESCRIPTION = "This is an automated repository created using Selenium."

# Initialize the WebDriver
driver = webdriver.Chrome()  # Adjust WebDriver to your browser
wait = WebDriverWait(driver, 15)

try:
    # Open GitHub login page
    driver.get("https://github.com/login")
    print("Opened GitHub login page")

    # Enter username
    username_field = wait.until(EC.presence_of_element_located((By.ID, "login_field")))
    username_field.send_keys(GITHUB_USERNAME)

    # Enter password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(GITHUB_PASSWORD)

    # Click on login button
    login_button = driver.find_element(By.NAME, "commit")
    login_button.click()

    # Wait for the user to be logged in by checking for the user's avatar (or another visible element)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'avatar-user')))
    print("Successfully logged in")

    # Navigate to "New repository" page
    driver.get("https://github.com/new")
    print("Navigated to the 'New repository' page")

    # Wait for the repository name field to be present
    repo_name_field = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='repository[name]']"))
    )

    # Fill the repository name
    repo_name_field.click()
    repo_name_field.clear()
    repo_name_field.send_keys(REPO_NAME)
    print(f"Repository name '{REPO_NAME}' entered")

    # Enter repository description (optional)
    if REPO_DESCRIPTION:
        description_field = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='repository[description]']"))
        )
        description_field.click()
        description_field.clear()
        description_field.send_keys(REPO_DESCRIPTION)
        print(f"Repository description entered: '{REPO_DESCRIPTION}'")

    # Ensure the "Create repository" button is clickable using a specific XPath
    create_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary') and contains(., 'Create repository')]"))
    )
    create_button.click()
    print("Clicked 'Create repository' button")

    # Wait for the repository page to load by checking if the URL contains the repository name
    wait.until(EC.url_contains(REPO_NAME))  # This ensures the page URL contains the repository name

    print(f"Repository '{REPO_NAME}' created successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Optional: Wait for 5 seconds before closing
    time.sleep(5)
    driver.quit()
