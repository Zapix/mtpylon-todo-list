# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Union, Annotated


@dataclass
class BoolTrue:
    class Meta:
        name = 'boolTrue'


@dataclass
class BoolFalse:
    class Meta:
        name = 'boolFalse'


Bool = Annotated[
    Union[BoolTrue, BoolFalse],
    'Bool'
]
