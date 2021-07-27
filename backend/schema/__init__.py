# -*- coding: utf-8 -*-
from mtpylon import Schema  # type: ignore


from .constructors import User
from .functions import register

mtpylon_schema = Schema(
    constructors=[User],
    functions=[register]
)

__all__ = [
    'mtpylon_schema'
]
