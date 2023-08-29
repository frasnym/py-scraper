import re
from selenium.webdriver.remote.webdriver import WebDriver

from models.product import Product

def get_by_url(driver: WebDriver, url:str)->Product:
    product = Product()

    driver.get(url) # Navigate to a website

    # Find an element on the page and extract data
    title_element = driver.find_element("css selector", "h1")
    product.title = title_element.text

    description_element = driver.find_element("css selector", ".eytdjj01")
    product.description = description_element.text

    price_element = driver.find_element("css selector", ".price")
    price_string = re.sub(r"\D", "", price_element.text) # Substitute all non-digit characters with empty string
    product.price = int(price_string)

    # Find all <img> tags by class name
    img_elements = driver.find_elements("css selector", ".css-1c345mg")
    # img_elements = driver.find_elements(By.XPATH, "//img[@data-testid='PDPMainImage']")

    # Iterate over the list of img elements
    for img_element in img_elements:
        image_url = img_element.get_attribute("src") # Get the value of the "src" attribute
        image_url = image_url.replace("100-square", "900") # Get bigger image
        product.images.append(image_url) # Print the image URL

    return product