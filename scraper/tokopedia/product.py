import re
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from models.product import Product


def get_by_url(driver: WebDriver, url: str) -> Product:
    product = Product()

    driver.get(url)  # Navigate to a website

    # Find an element on the page and extract data
    wait = WebDriverWait(driver, 10)  # Wait timeout, Adjust the timeout as needed

    title_element = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )  # Wait until the form class is found
    # title_element = driver.find_element("css selector", "h1")
    product.title = title_element.text

    description_element = driver.find_element(By.CLASS_NAME, "eytdjj01")
    product.description = description_element.text

    price_element = driver.find_element(By.CLASS_NAME, "price")
    price_string = re.sub(
        r"\D", "", price_element.text
    )  # Substitute all non-digit characters with empty string
    product.price = int(price_string)

    # Find all <img> tags by class name
    img_elements = driver.find_elements(By.CLASS_NAME, "css-1c345mg")
    # img_elements = driver.find_elements(By.XPATH, "//img[@data-testid='PDPMainImage']")

    # Iterate over the list of img elements
    for img_element in img_elements:
        image_url = img_element.get_attribute(
            "src"
        )  # Get the value of the "src" attribute
        image_url = image_url.replace("100-square", "900")  # Get bigger image
        image_url = image_url.replace(".webp?ect=4g", "")  # Unnecessary extension
        product.images.append(image_url)  # Print the image URL

    return product
