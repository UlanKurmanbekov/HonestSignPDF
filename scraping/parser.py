

class ProductParser:
    def __init__(self, raw_data: dict[str, any]) -> None:
        self.raw_data = raw_data
        self.parsed_data = {}

    def parse(self) -> dict[str, str]:
        content = self.raw_data.get("content", [{}])[0]
        self.parsed_data["gtin"] = content.get("gtin")
        self.parsed_data["manufacturer_name"] = content.get("manufacturerShortName")

        self._parse_attributes(content.get("attributes", []))

        return self.parsed_data

    def _parse_attributes(self, attributes: list[dict[str, str]]) -> None:
        attribute_map = {
            "Размер одежды / изделия": "size",
            "Цвет": "color",
            "Полное наименование товара": "name"
        }

        for attribute in attributes:
            attribute_name = attribute.get("attributeTypeName")

            if attribute_name in attribute_map:
                self.parsed_data[attribute_map[attribute_name]] = attribute.get("value")
