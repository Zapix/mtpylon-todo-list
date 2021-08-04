# -*- coding: utf-8 -*-
from aiohttp.web import Request
from mtpylon.exceptions import RpcCallError  # type: ignore
from mtpylon.contextvars import auth_key_var

from users.utils import register_user, remember_user
from ..constructors import User, RegisteredUser


async def register(request: Request, nickname: str, password: str) -> User:
    """
    Tries to register user
    Raises:
        RpcCallError - on registration failure
    """
    try:
        user = await register_user(nickname, password)
    except ValueError as e:
        raise RpcCallError(
            error_code=400,
            error_message=str(e)
        )

    auth_key = auth_key_var.get()

    await remember_user(user, auth_key)

    return RegisteredUser(
        id=user.id,
        nickname=user.nickname
    )
