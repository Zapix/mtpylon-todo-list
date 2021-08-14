# -*- coding: utf-8 -*-
import pytest
from contextlib import ExitStack
from unittest.mock import AsyncMock, MagicMock, patch

from mtpylon.crypto import AuthKey
from mtpylon.exceptions import RpcCallError
from mtpylon.contextvars import auth_key_var

from schema.functions.edit_task_title_func import edit_task_title
from schema.constructors import Task
from users.models import User
from todos.models import Task as TaskModel


@pytest.mark.asyncio
async def test_edit_task_not_found(
    user: User,
    mtpylon_auth_key: AuthKey,
):
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)

    get_task_for_user = AsyncMock(return_value=None)

    change_title = AsyncMock()

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
                'schema.functions.edit_task_title_func.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.edit_task_title_func.get_task_for_user',
                get_task_for_user
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.edit_task_title_func.change_title',
                change_title
            )
        )

        with pytest.raises(RpcCallError):
            await edit_task_title(request, -1, 'hello world')

        change_title.assert_not_awaited()


@pytest.mark.asyncio
async def test_edit_task_value_error(
    user: User,
    mtpylon_auth_key: AuthKey,
    task: TaskModel,
):
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)

    get_task_for_user = AsyncMock(return_value=task)

    change_title = AsyncMock(side_effect=ValueError('Wrong title'))

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
                'schema.functions.edit_task_title_func.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.edit_task_title_func.get_task_for_user',
                get_task_for_user
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.edit_task_title_func.change_title',
                change_title
            )
        )

        with pytest.raises(RpcCallError):
            await edit_task_title(request, task.id, 'hello world')

        change_title.assert_awaited()


@pytest.mark.asyncio
async def test_edit_task_title_success(
    user: User,
    mtpylon_auth_key: AuthKey,
    task: TaskModel,

):
    new_title = 'hello world'
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)

    get_task_for_user = AsyncMock(return_value=task)

    change_title = AsyncMock(return_value=MagicMock(
        id=task.id,
        title=new_title,
        completed=task.completed
    ))

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
                'schema.functions.edit_task_title_func.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.edit_task_title_func.get_task_for_user',
                get_task_for_user
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.edit_task_title_func.change_title',
                change_title
            )
        )
        response = await edit_task_title(request, task.id, new_title)

    change_title.assert_awaited()

    assert isinstance(response, Task)
    assert response.id == task.id
    assert response.title == new_title
