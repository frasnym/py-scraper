from helpers.file_writer import write_to_file
from models.product import ProductShopee
from scraper.tokopedia.product import get_by_url

try:
    product = get_by_url("https://www.tokopedia.com/mofan/kipas-angin-usb-mini-2-baling-flexibel-fan-usb-portable-pink?extParam=ivf%3Dfalse%26src%3Dsearch")
    product_shopee = ProductShopee.from_product(product)
    print(product_shopee.__str__())

    write_to_file(product_shopee.__str__(), "products.json") # Write output to file
except ValueError as e:
    print("An error occurred:", str(e))


    