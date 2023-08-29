from scraper.tokopedia.product import get_by_url

try:
    get_by_url("https://www.tokopedia.com/mofan/kipas-angin-usb-mini-2-baling-flexibel-fan-usb-portable-pink?extParam=ivf%3Dfalse%26src%3Dsearch")
except ValueError as e:
    print("An error occurred:", str(e))


    