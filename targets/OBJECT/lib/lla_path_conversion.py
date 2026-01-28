from datetime import datetime, timezone
from openc3.conversions.conversion import Conversion


class LlaPathConversion(Conversion):
    """Sets the HTTP_PATH for LLA API with current UTC timestamp."""

    def __init__(self, object_id="25544"):
        super().__init__()
        self.object_id = object_id

    def call(self, value, packet, _buffer):
        # Use current UTC time in ISO 8601 format
        now = datetime.now(timezone.utc)
        timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        return f"/v2/sat/{self.object_id}/lla/{timestamp}"

    def __str__(self):
        return f'LlaPathConversion("{self.object_id}")'

    def to_config(self, read_or_write):
        return f'{read_or_write}_CONVERSION lla_path_conversion.py "{self.object_id}"\n'
