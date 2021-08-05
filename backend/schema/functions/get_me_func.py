# -*- coding: utf-8 -*-
from aiohttp.web import Request
from mtpylon.contextvars import auth_key_var

from ..constructors import User, RegisteredUser, AnonymousUser
from users.utils import get_user_by_auth_key


async def get_me(request: Request) -> User:
    auth_key = auth_key_var.get()
    me = await get_user_by_auth_key(auth_key)

    if me is None:
        return AnonymousUser()

    return RegisteredUser(
        id=me.id,
        nickname=me.nickname
    )
