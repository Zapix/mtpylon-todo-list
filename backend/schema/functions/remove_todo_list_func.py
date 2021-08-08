# -*- coding: utf-8 -*-
from typing import cast

from aiohttp.web import Request
from mtpylon.contextvars import auth_key_var
from mtpylon.exceptions import RpcCallError

from ..constructors import Bool, BoolTrue
from users.models import User
from users.utils import get_user_by_auth_key
from todos.utils import get_todo_list_for_user, delete_todo_list


async def remove_todo_list(request: Request, todo_list_id: int) -> Bool:
    auth_key = auth_key_var.get()
    user = await get_user_by_auth_key(auth_key)

    user = cast(User, user)

    todo_list = await get_todo_list_for_user(user, todo_list_id)

    if todo_list is None:
        raise RpcCallError(
            error_code=404,
            error_message="Todo list not found"
        )

    await delete_todo_list(todo_list)

    return BoolTrue()
