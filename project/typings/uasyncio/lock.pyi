"""
Module: 'uasyncio.lock' on micropython-v1.27.0-esp32-ESP32_GENERIC_S3-SPIRAM_OCT
"""

# MCU: {'variant': 'SPIRAM_OCT', 'build': '', 'arch': 'xtensawin', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'board_id': 'ESP32_GENERIC_S3-SPIRAM_OCT', 'mpy': 'v6.3', 'ver': '1.27.0', 'family': 'micropython', 'cpu': 'ESP32S3', 'version': '1.27.0'}
# Stubber: v1.29.0
from __future__ import annotations

from typing import Generator

from _typeshed import Incomplete

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...
    def acquire(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...
    def __init__(self, *argv, **kwargs) -> None: ...
