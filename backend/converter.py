# -*- coding: utf-8 -*-
from mtpylon.types import long


def int64_to_long(value: int) -> long:
    value_bytes = value.to_bytes(8, 'little', signed=False)
    return long(int.from_bytes(value_bytes, 'little', signed=True))


def long_to_int64(value: long) -> int:
    value_bytes = value.to_bytes(8, 'little', signed=True)
    return int.from_bytes(value_bytes, 'little', signed=False)
