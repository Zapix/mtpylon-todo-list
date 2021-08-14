# -*- coding: utf-8 -*-
import pytest
from contextlib import ExitStack
from unittest.mock import AsyncMock, MagicMock, patch
from mtpylon.crypto import AuthKey
from mtpylon.contextvars import auth_key_var
from mtpylon.exceptions import RpcCallError

from schema.functions.create_task_func import create_task
from schema.constructors import Task
from schema.utils.converter import to_bool
from users.models import User
from todos.models import TodoList


@pytest.mark.asyncio
async def test_create_task_rpc_error_not_found(
    user: User,
    mtpylon_auth_key: AuthKey,
):
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)
    get_todo_list_for_user = AsyncMock(return_value=None)

    request = MagicMock()

    with ExitStack() as patcher:
        patcher.enter_context(
            patch(
                'schema.utils.decorators.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.create_task_func.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.create_task_func.get_todo_list_for_user',
                get_todo_list_for_user
            )
        )

        with pytest.raises(RpcCallError):
            await create_task(request, 12, 'hello title')


@pytest.mark.asyncio
async def test_create_task_rpc_error(
    user: User,
    todo_list: TodoList,
    mtpylon_auth_key: AuthKey,
):
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)
    get_todo_list_for_user = AsyncMock(return_value=todo_list)
    create_task_util = AsyncMock(side_effect=ValueError('Empty title'))

    request = MagicMock()

    with ExitStack() as patcher:
        patcher.enter_context(
            patch(
                'schema.utils.decorators.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.create_task_func.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.create_task_func.get_todo_list_for_user',
                get_todo_list_for_user
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.create_task_func.create_task_util',
                create_task_util
            )
        )

        with pytest.raises(RpcCallError):
            await create_task(request, todo_list.id, '')


@pytest.mark.asyncio
async def test_create_task_success(
    user: User,
    todo_list: TodoList,
    mtpylon_auth_key: AuthKey
):
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)
    get_todo_list_for_user = AsyncMock(return_value=todo_list)

    created_task = MagicMock(id=1, title='first task', completed=False)
    create_task_util = AsyncMock(return_value=created_task)

    request = MagicMock()

    with ExitStack() as patcher:
        patcher.enter_context(
            patch(
                'schema.utils.decorators.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.create_task_func.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.create_task_func.get_todo_list_for_user',
                get_todo_list_for_user
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.create_task_func.create_task_util',
                create_task_util
            )
        )

        returned_task = await create_task(request, todo_list.id, 'first task')

    assert isinstance(returned_task, Task)
    assert returned_task.id == 1
    assert returned_task.title == 'first task'
    assert not to_bool(returned_task.completed)
