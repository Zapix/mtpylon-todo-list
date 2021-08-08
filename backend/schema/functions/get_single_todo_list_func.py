# -*- coding: utf-8 -*-
from typing import cast

from aiohttp.web import Request
from mtpylon.contextvars import auth_key_var
from mtpylon.exceptions import RpcCallError

from ..constructors import TodoList
from ..utils.decorators import login_required
from todos.utils import get_todo_list_for_user
from users.models import User
from users.utils import get_user_by_auth_key


@login_required
async def get_single_todo_list(
    request: Request,
    todo_list_id: int
) -> TodoList:
    auth_key = auth_key_var.get()
    user = await get_user_by_auth_key(auth_key)
    user = cast(User, user)

    todo_list = await get_todo_list_for_user(user, todo_list_id)

    if todo_list is None:
        raise RpcCallError(
            error_code=404,
            error_message="Todo list not found"
        )

    return TodoList(
        id=todo_list.id,
        title=todo_list.title
    )
