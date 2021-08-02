# -*- coding: utf-8 -*-
from aiohttp.web import Request
from mtpylon.crypto import AuthKey  # type: ignore
from mtpylon.exceptions import RpcCallError  # type: ignore
from mtpylon.contextvars import auth_key_var  # type: ignore

from users.utils import login_user, remember_user
from ..constructors import User, RegisteredUser


async def login(request: Request, nickname: str, password: str) -> User:
    try:
        user = await login_user(nickname, password)
    except ValueError as e:
        raise RpcCallError(error_code=401, error_message=str(e))

    auth_key: AuthKey = auth_key_var.get()
    await remember_user(user, auth_key)

    return RegisteredUser(id=user.id, nickname=nickname)
