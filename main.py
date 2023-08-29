import json
from helpers.file_reader import read_file_lines
from helpers.file_writer import write_to_csv, write_to_file
from models.product import ProductShopee
from scraper.driver.driver import create_driver
from scraper.tokopedia.product import get_by_url


def scrape_tokopedia_bulk() -> list[ProductShopee]:
    # Read input from file
    file_path = "dist/input/tokopedia_urls.txt"
    lines = read_file_lines(file_path)

    driver = create_driver()

    products: list[ProductShopee] = []
    for line in lines:
        product = get_by_url(driver, line.strip())
        product_shopee = ProductShopee.from_product(product)
        products.append(product_shopee)

    driver.quit()

    return products


try:
    products = scrape_tokopedia_bulk()

    # write to json
    json_string = json.dumps(
        [obj.__dict__ for obj in products]
    )  # Convert the array to a JSON string
    write_to_file(json_string, "products.json")

    # write to csv
    data: list[list[str]] = []
    data.append(products[0].__dict__.keys())

    for element in products:
        data.append(element.__dict__.values())

    write_to_csv(data, "products.csv")


except ValueError as e:
    print("An error occurred:", str(e))
