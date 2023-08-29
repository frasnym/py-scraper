import json, math


class Product:
    def __init__(self):
        self.title: str = ""
        self.description: str = ""
        self.images: list[str] = []
        self.price: int = 0

    def __str__(self):
        return json.dumps(self.__dict__)


class ProductShopee:
    def __init__(self) -> None:
        self.category: str = ""
        self.product_name: str = ""
        self.product_description: str = ""
        self.parent_sku: str = ""
        self.dangerous_products: str = ""
        self.variation_integration_code: str = ""
        self.variation_name_1: str = ""
        self.variant_for_variation_1: str = ""
        self.product_photos_per_variant: str = ""
        self.variation_name_2: str = ""
        self.variant_for_variation_2: str = ""
        self.price: int = 0
        self.stock: int = 1
        self.variation_code: str = ""
        self.size_guide: str = ""
        self.cover_photo: str = ""
        self.product_photos_1: str = ""
        self.product_photos_2: str = ""
        self.product_photos_3: str = ""
        self.product_photos_4: str = ""
        self.product_photos_5: str = ""
        self.product_photos_6: str = ""
        self.product_photos_7: str = ""
        self.product_photos_8: str = ""
        self.heavy: str = "1000"
        self.long: str = ""
        self.wide: str = ""
        self.tall: str = ""
        self.same_day: str = "Aktif"
        self.regular_cashless: str = "Aktif"
        self.economical: str = "Aktif"
        self.shipped_on_pre_order: str = ""
        self.failed_reasons: str = ""

        return

    def __str__(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def from_product(self, prd: Product):
        product_shopee = self()
        product_shopee.product_name = prd.title
        product_shopee.product_description = prd.description
        product_shopee.cover_photo = prd.images[0]

        prd.images = prd.images[1:]
        for i in range(len(prd.images)):
            if i >= 8:
                break
            setattr(product_shopee, f"product_photos_{i+1}", prd.images[i])

        product_shopee.price = math.ceil(prd.price * 1.15)
        if product_shopee.price < 2000:
            product_shopee.price = 2000

        return product_shopee
