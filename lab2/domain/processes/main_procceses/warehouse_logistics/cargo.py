from dataclasses import dataclass
from typing import Literal

from core.enums.material import Material
from core.enums.product import Product


@dataclass
class Cargo:
    items: dict[Material | Product, int]
    origin: str
    destiantion: str
    customs_status: Literal[
        "domestic", "export_cleared", "import_cleared", "custom_required"
    ]
