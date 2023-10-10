from dataclasses import dataclass


@dataclass
class Trademark:
    application_number: str
    register_status: str
    tm_division_code: str
    product_name: str | None
    product_name_eng: str | None
    image_url: str | None
