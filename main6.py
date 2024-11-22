from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

def get_web_driver(browser_type='chrome', driver_path=None):
    """
    Returns a Selenium WebDriver instance based on the browser type.

    :param browser_type: str, Type of browser ('chrome', 'firefox', 'edge')
    :param driver_path: str, Path to the specific WebDriver executable
    :return: WebDriver instance
    """
    if browser_type == 'chrome':
        service = Service(driver_path)
        return webdriver.Chrome(service=service)
    elif browser_type == 'firefox':
        service = FirefoxService(driver_path)
        return webdriver.Firefox(service=service)
    elif browser_type == 'edge':
        service = EdgeService(driver_path)
        return webdriver.Edge(service=service)
    else:
        raise ValueError(f"Unsupported browser type: {browser_type}")
