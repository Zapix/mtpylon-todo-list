# -*- coding: utf-8 -*-
from mtpylon import Schema  # type: ignore


from .constructors import User
from .functions import register, login

mtpylon_schema = Schema(
    constructors=[User],
    functions=[
        register,
        login,
    ]
)

__all__ = [
    'mtpylon_schema'
]
