# -*- coding: utf-8 -*-
from typing import cast
from aiohttp.web import Request
from mtpylon.crypto import AuthKey
from mtpylon.contextvars import auth_key_var

from ..constructors import TodoList, TodoListsResult
from ..utils.decorators import login_required
from users.models import User
from users.utils import get_user_by_auth_key
from todos.utils import get_todo_lists as get_todo_lists_util


@login_required
async def get_todo_lists(request: Request) -> TodoListsResult:
    auth_key: AuthKey = auth_key_var.get()

    user = await get_user_by_auth_key(auth_key)
    user = cast(User, user)

    results = await get_todo_lists_util(user)
    return TodoListsResult(
        todo_lists=[
            TodoList(id=item.id, title=item.title)
            for item in results
        ]
    )
