from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
    chrome_options = Options() # Create ChromeOptions object
    driver = webdriver.Chrome(options=chrome_options) # Create a new instance of the Chrome driver with headless option
    return driver