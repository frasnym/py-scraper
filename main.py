import json
from helpers.file_reader import read_file_lines
from helpers.file_writer import write_to_file
from models.product import ProductShopee
from scraper.driver.driver import create_driver
from scraper.tokopedia.product import get_by_url

try:
    # Read input from file
    file_path = 'input/tokopedia_urls.txt'
    lines = read_file_lines(file_path)

    driver = create_driver()

    products: list[ProductShopee] = []
    for line in lines:
        product = get_by_url(driver, line.strip())
        product_shopee = ProductShopee.from_product(product)
        products.append(product_shopee)

    driver.quit()

    json_string = json.dumps([obj.__dict__ for obj in products]) # Convert the array to a JSON string
    write_to_file(json_string, "products.json")
    
except ValueError as e:
    print("An error occurred:", str(e))


    