# -*- coding: utf-8 -*-
from typing import cast

from aiohttp.web import Request
from mtpylon.exceptions import RpcCallError
from mtpylon.contextvars import auth_key_var

from todos.utils import get_task_for_user, change_title
from users.models import User
from users.utils import get_user_by_auth_key
from ..constructors import Task
from ..utils.decorators import login_required
from ..utils.converter import from_task_model


@login_required
async def edit_task_title(request: Request, task_id: int, title: str) -> Task:
    auth_key = auth_key_var.get()
    user = await get_user_by_auth_key(auth_key)
    user = cast(User, user)

    task = await get_task_for_user(user, task_id)

    if task is None:
        raise RpcCallError(
            error_code=404,
            error_message=f'Task with id {task_id} not found'
        )

    try:
        updated_task = await change_title(task, title)
    except ValueError as e:
        raise RpcCallError(
            error_code=400,
            error_message=str(e)
        )

    return from_task_model(updated_task)
