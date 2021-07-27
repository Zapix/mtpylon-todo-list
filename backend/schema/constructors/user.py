# -*- coding: utf-8 -*-
from typing import Union, Annotated
from dataclasses import dataclass


@dataclass
class AnonymousUser:
    class Meta:
        name = 'anonymous_user'


@dataclass
class RegisteredUser:
    id: int
    nickname: str

    class Meta:
        name = 'registered_user'

        order = ('id', 'nickname')


User = Annotated[
    Union[
        AnonymousUser,
        RegisteredUser
    ],
    'User'
]
