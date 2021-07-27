# -*- coding: utf-8 -*-
from aiohttp.web import Request
from mtpylon.exceptions import RpcCallError  # type: ignore

from users.utils import register_user
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

    return RegisteredUser(
        id=user.id,
        nickname=user.nickname
    )
