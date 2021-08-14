# -*- coding: utf-8 -*-
from typing import cast

from aiohttp.web import Request
from mtpylon.contextvars import auth_key_var
from mtpylon.exceptions import RpcCallError

from users.models import User
from users.utils import get_user_by_auth_key
from todos.utils import delete_task, get_task_for_user
from ..constructors import Bool, BoolTrue
from ..utils.decorators import login_required


@login_required
async def remove_task(request: Request, task_id: int) -> Bool:
    auth_key = auth_key_var.get()

    user = await get_user_by_auth_key(auth_key)
    user = cast(User, user)

    task = await get_task_for_user(user, task_id)

    if task is None:
        raise RpcCallError(
            error_code=404,
            error_message='Task not found'
        )

    await delete_task(task)

    return BoolTrue()
