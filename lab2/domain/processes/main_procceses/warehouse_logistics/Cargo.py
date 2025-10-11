from dataclasses import dataclass
from typing import Literal

from core.enums.Material import Material
from core.enums.Product import Product


@dataclass
class Cargo:
    items: dict[Material | Product, int]
    origin: str
    destination: str
    customs_status: Literal[
        "domestic", "export_cleared", "import_cleared", "custom_required"
    ]
