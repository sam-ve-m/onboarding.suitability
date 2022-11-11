from http import HTTPStatus

from decouple import config
from httpx import AsyncClient

from ...domain.exceptions.transports.exception import (
    DeviceInfoRequestFailed,
    DeviceInfoNotSupplied,
)
from ...domain.models.device_info import DeviceInfo


class DeviceSecurity:
    @staticmethod
    async def decrypt_device_info(device_info: str) -> DeviceInfo:
        if not device_info:
            raise DeviceInfoNotSupplied()
        body = {"deviceInfo": device_info}
        async with AsyncClient() as httpx_client:
            request_result = await httpx_client.post(
                config("DEVICE_SECURITY_DECRYPT_DEVICE_INFO_URL"), json=body
            )
            if request_result.status_code != HTTPStatus.OK:
                raise DeviceInfoRequestFailed()
        device_info_decrypted = request_result.json().get("deviceInfo")
        device_info = DeviceInfo(**device_info_decrypted)
        return device_info

    @staticmethod
    async def generate_device_id(device_info: str) -> str:
        if not device_info:
            raise DeviceInfoNotSupplied()
        body = {"deviceInfo": device_info}
        async with AsyncClient() as httpx_client:
            request_result = await httpx_client.post(
                config("DEVICE_SECURITY_DEVICE_ID_URL"), json=body
            )
            if request_result.status_code != HTTPStatus.OK:
                raise DeviceInfoRequestFailed()
        device_id = request_result.json().get("deviceID")
        return device_id
