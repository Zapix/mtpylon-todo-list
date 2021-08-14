# -*- coding: utf-8 -*-
import pytest
from contextlib import ExitStack
from unittest.mock import AsyncMock, MagicMock, patch


from mtpylon.crypto import AuthKey
from mtpylon.exceptions import RpcCallError
from mtpylon.contextvars import auth_key_var


from schema.functions.remove_task_func import remove_task
from schema.utils.converter import to_bool
from users.models import User
from todos.models import Task


@pytest.mark.asyncio
async def test_remove_task_not_found(
    user: User,
    mtpylon_auth_key: AuthKey
):
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)

    get_task_for_user = AsyncMock(return_value=None)

    delete_task = AsyncMock()

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
                'schema.functions.remove_task_func.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.remove_task_func.get_task_for_user',
                get_task_for_user
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.remove_task_func.delete_task',
                delete_task
            )
        )

        with pytest.raises(RpcCallError):
            await remove_task(request, -4)

    delete_task.assert_not_awaited()


@pytest.mark.asyncio
async def test_remove_task_success(
    user: User,
    mtpylon_auth_key: AuthKey,
    task: Task
):
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)

    get_task_for_user = AsyncMock(return_value=task)

    delete_task = AsyncMock()

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
                'schema.functions.remove_task_func.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.remove_task_func.get_task_for_user',
                get_task_for_user
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.remove_task_func.delete_task',
                delete_task
            )
        )

        response = await remove_task(request, task.id)

    assert to_bool(response)
