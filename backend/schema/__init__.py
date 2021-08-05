# -*- coding: utf-8 -*-
from mtpylon import Schema


from .constructors import User
from .functions import register, login, get_me

mtpylon_schema = Schema(
    constructors=[User],
    functions=[
        register,
        login,
        get_me,
    ]
)

__all__ = [
    'mtpylon_schema'
]
