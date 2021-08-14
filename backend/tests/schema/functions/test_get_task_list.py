# -*- coding: utf-8 -*-
import pytest
from contextlib import ExitStack
from unittest.mock import AsyncMock, MagicMock, patch

from mtpylon.contextvars import auth_key_var
from mtpylon.crypto import AuthKey
from mtpylon.exceptions import RpcCallError

from schema.functions.get_task_list_func import get_task_list
from schema.constructors import TaskList, Task
from users.models import User
from todos.models import TodoList


@pytest.mark.asyncio
async def test_get_task_list_not_found(
    user: User,
    mtpylon_auth_key: AuthKey,
):
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)

    request = MagicMock()

    get_todo_list_for_user = AsyncMock(return_value=None)
    get_tasks_for_todo_list = AsyncMock()

    with ExitStack() as patcher:
        patcher.enter_context(
            patch(
                'schema.utils.decorators.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.get_task_list_func.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.get_task_list_func.get_todo_list_for_user',
                get_todo_list_for_user
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.get_task_list_func.get_tasks_for_todo_list',
                get_tasks_for_todo_list
            )
        )

        with pytest.raises(RpcCallError):
            await get_task_list(request, -3)

    get_todo_list_for_user.assert_awaited()
    get_tasks_for_todo_list.assert_not_awaited()


@pytest.mark.asyncio
async def test_get_task_list_ok(
    user: User,
    mtpylon_auth_key: AuthKey,
    todo_list: TodoList,
):
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)

    request = MagicMock()

    get_todo_list_for_user = AsyncMock(return_value=todo_list)
    get_tasks_for_todo_list = AsyncMock(return_value=[
        MagicMock(id=1, title='First', completed=True),
        MagicMock(id=2, title='Second', completed=True),
        MagicMock(id=3, title='Third', completed=True),
    ])

    with ExitStack() as patcher:
        patcher.enter_context(
            patch(
                'schema.utils.decorators.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.get_task_list_func.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.get_task_list_func.get_todo_list_for_user',
                get_todo_list_for_user
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.get_task_list_func.get_tasks_for_todo_list',
                get_tasks_for_todo_list
            )
        )

        response = await get_task_list(
            request,
            todo_list_id=todo_list.id
        )

    assert isinstance(response, TaskList)
    assert len(response.tasks) == 3
    assert isinstance(response.tasks[0], Task)

    get_todo_list_for_user.assert_awaited()
    get_tasks_for_todo_list.assert_awaited()
