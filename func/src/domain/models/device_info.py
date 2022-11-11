from typing import Optional

from decouple import config


class DeviceInfo:
    def __init__(
        self,
        ip: str,
        latitude: float,
        longitude: float,
        precision: Optional[float] = None,
        **kwargs
    ):
        self.ip = ip
        self.latitude = latitude
        self.longitude = longitude
        self.precision = precision
        if precision is None:
            self.precision = float(config("DEFAULT_PRECISION_VALUE"))
