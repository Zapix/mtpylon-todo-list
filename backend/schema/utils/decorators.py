# -*- coding: utf-8 -*-
from typing import Coroutine, Callable
from functools import wraps

from aiohttp.web import Request
from mtpylon.crypto import AuthKey
from mtpylon.contextvars import auth_key_var
from mtpylon.exceptions import RpcCallError

from users.utils import get_user_by_auth_key


MtpylonFunc = Callable[
    ...,
    Coroutine
]


def login_required(async_func: MtpylonFunc) -> MtpylonFunc:
    """
    Decorator to check that
    """
    @wraps(async_func)
    async def wrapper(request: Request, *args, **kwargs):
        auth_key: AuthKey = auth_key_var.get()

        user = await get_user_by_auth_key(auth_key)

        if user is None:
            raise RpcCallError(
                error_code=401,
                error_message='User not authorized'
            )

        return await async_func(request, *args, **kwargs)

    return wrapper
