# -*- coding: utf-8 -*-
import pytest
from contextlib import ExitStack
from unittest.mock import AsyncMock, MagicMock, patch

from mtpylon.crypto import AuthKey
from mtpylon.exceptions import RpcCallError
from mtpylon.contextvars import auth_key_var

from schema.functions.set_as_completed_func import set_as_completed
from schema.constructors import Task
from schema.utils.converter import to_bool
from users.models import User
from todos.models import Task as TaskModel


@pytest.mark.asyncio
async def test_set_as_completed_not_found(
    user: User,
    mtpylon_auth_key: AuthKey,
):
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)

    get_task_for_user = AsyncMock(return_value=None)

    mark_completed = AsyncMock()

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
                'schema.functions.set_as_completed_func.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.set_as_completed_func.get_task_for_user',
                get_task_for_user
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.set_as_completed_func.mark_completed',
                mark_completed
            )
        )

        with pytest.raises(RpcCallError):
            await set_as_completed(request, -4)

        mark_completed.assert_not_awaited()


@pytest.mark.asyncio
async def test_set_as_completed_success(
    user: User,
    mtpylon_auth_key: AuthKey,
    task: TaskModel
):
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)

    get_task_for_user = AsyncMock(return_value=task)

    mark_completed = AsyncMock(return_value=MagicMock(
        id=task.id,
        title=task.title,
        completed=True
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
                'schema.functions.set_as_completed_func.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.set_as_completed_func.get_task_for_user',
                get_task_for_user
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.set_as_completed_func.mark_completed',
                mark_completed
            )
        )

        updated_task = await set_as_completed(request, task.id)

    assert isinstance(updated_task, Task)
    assert updated_task.id == task.id
    assert updated_task.title == task.title
    assert to_bool(updated_task.completed)
