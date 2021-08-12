# -*- coding: utf-8 -*-
from ..constructors.bool import Bool, BoolTrue, BoolFalse


def from_bool(value: bool) -> Bool:
    if value:
        return BoolTrue()

    return BoolFalse()


def to_bool(value: Bool) -> bool:
    return value == BoolTrue()
