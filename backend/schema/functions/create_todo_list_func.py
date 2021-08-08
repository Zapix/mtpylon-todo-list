# -*- coding: utf-8 -*-
from typing import cast

from aiohttp.web import Request
from mtpylon.exceptions import RpcCallError
from mtpylon.contextvars import auth_key_var

from ..constructors import TodoList
from ..utils.decorators import login_required
from todos.utils import create_todo_list as create_todo_list_util
from users.models import User
from users.utils import get_user_by_auth_key


@login_required
async def create_todo_list(request: Request, title: str) -> TodoList:
    """
    Creates todo list for logged in user
    """
    if len(title) == 0:
        raise RpcCallError(
            error_code=400,
            error_message='Title should not been empty'
        )

    auth_key = auth_key_var.get()
    user = await get_user_by_auth_key(auth_key)
    user = cast(User, user)

    todo_list = await create_todo_list_util(user, title)

    return TodoList(
        id=todo_list.id,
        title=todo_list.title
    )
