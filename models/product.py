import json


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
        self.sku: str = ""
        self.variation_integration_code: str = ""
        self.variation_name_1: str = ""
        self.variant_for_variation_1: str = ""
        self.product_photos_per_variant: str = ""
        self.variation_name_2: str = ""
        self.variant_for_variation_2: str = ""
        self.price: int = 0
        self.stock: str = ""
        self.variation_code: str = ""
        self.hs_code: str = ""
        self.tax_code: str = ""
        self.cover_photo: str = ""
        self.product_photos_1: str = ""
        self.product_photos_2: str = ""
        self.product_photos_3: str = ""
        self.product_photos_4: str = ""
        self.product_photos_5: str = ""
        self.product_photos_6: str = ""
        self.product_photos_7: str = ""
        self.product_photos_8: str = ""
        self.heavy: str = ""
        self.long: str = ""
        self.wide: str = ""
        self.tall: str = ""
        self.delivery_service_1: str = ""
        self.delivery_service_2: str = ""
        self.delivery_service_3: str = ""
        self.term_shipped_in_pre_order: str = ""
        self.shipped_on_pre_order: str = ""
        self.brand: str = ""
        self.benefits_of_hair_care_free_text: str = ""
        self.expiration_date_date: str = ""
        self.arm_length_single_dropdown: str = ""
        self.formulation_optional_with_own_filling: str = ""
        self.materials_multiple_options: str = ""
        self.occasion_multiple_choices_with_own_filling: str = ""
        self.capacity_quantitative_free_text: str = ""
        self.monitor_screen_size_quantitative_selection_by_own_entry: str = ""
        self.screen_size_multiple_quantitative_choices_with_self_fill: str = ""
        self.country_of_origin: str = ""
        self.manufacturing_details: str = ""
        self.packer_details: str = ""
        self.importer_details: str = ""
        return

    def __str__(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def from_product(self, prd: Product):
        product_shopee = self()
        product_shopee.product_name = prd.title
        product_shopee.product_description = prd.description

        for i in range(len(prd.images)):
            if i >= 8:
                break
            setattr(product_shopee, f"product_photos_{i+1}", prd.images[i])

        product_shopee.price = prd.price

        return product_shopee
