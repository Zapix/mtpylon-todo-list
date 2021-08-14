# -*- coding: utf-8 -*-
from typing import cast

from aiohttp.web import Request
from mtpylon.contextvars import auth_key_var
from mtpylon.exceptions import RpcCallError

from ..constructors import Task
from ..utils.decorators import login_required
from ..utils.converter import from_task_model
from users.models import User
from users.utils import get_user_by_auth_key
from todos.utils import get_todo_list_for_user, create_task as create_task_util


@login_required
async def create_task(request: Request, todo_list_id: int, title: str) -> Task:
    auth_key = auth_key_var.get()
    user = await get_user_by_auth_key(auth_key)
    user = cast(User, user)

    todo_list = await get_todo_list_for_user(user, todo_list_id)

    if todo_list is None:
        raise RpcCallError(
            error_code=404,
            error_message=f"ToDo with id: {todo_list_id} List not found"
        )

    try:
        task = await create_task_util(todo_list, title)
    except ValueError as e:
        raise RpcCallError(
            error_code=400,
            error_message=str(e)
        )

    return from_task_model(task)
