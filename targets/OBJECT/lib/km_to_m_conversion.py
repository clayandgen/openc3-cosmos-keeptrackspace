from openc3.conversions.conversion import Conversion


class KmToMConversion(Conversion):
    """Converts a value from kilometers to meters by reading a source item and multiplying by 1000."""

    def __init__(self, source_item):
        super().__init__()
        self.source_item = source_item
        self.converted_type = "FLOAT"
        self.converted_bit_size = 64
        self.params = [source_item]

    def call(self, value, packet, buffer):
        km_value = packet.read(self.source_item)
        if km_value is None:
            return None
        return float(km_value) * 1000.0

    def __str__(self):
        return f"KmToMConversion({self.source_item})"

    def to_config(self, read_or_write):
        return f"    {read_or_write}_CONVERSION km_to_m_conversion.py {self.source_item}\n"
