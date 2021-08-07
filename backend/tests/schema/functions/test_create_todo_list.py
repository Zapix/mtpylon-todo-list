# -*- coding: utf-8 -*-
import pytest
from contextlib import ExitStack
from unittest.mock import AsyncMock, MagicMock, patch
from mtpylon.contextvars import auth_key_var
from mtpylon.crypto import AuthKey
from mtpylon.exceptions import RpcCallError

from schema.constructors import TodoList
from schema.functions.create_todo_list_func import create_todo_list
from users.models import User


@pytest.mark.asyncio
async def test_create_todo_list_rpc_error(
    user: User,
    mtpylon_auth_key: AuthKey
):
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)

    request = MagicMock()

    create_todo_list_util = AsyncMock()

    with ExitStack() as patcher:
        patcher.enter_context(
            patch(
                'schema.utils.decorators.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.create_todo_list_func.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.create_todo_list_func.create_todo_list_util',
                create_todo_list_util
            )
        )
        with pytest.raises(RpcCallError):
            await create_todo_list(request, title='')

    create_todo_list_util.assert_not_awaited()


@pytest.mark.asyncio
async def test_create_todo_list_success(
    user: User,
    mtpylon_auth_key: AuthKey
):
    auth_key_var.set(mtpylon_auth_key)

    get_user_by_auth_key = AsyncMock(return_value=user)

    request = MagicMock()

    todo_list = AsyncMock(id=12, title='example')
    create_todo_list_util = AsyncMock(return_value=todo_list)

    with ExitStack() as patcher:
        patcher.enter_context(
            patch(
                'schema.utils.decorators.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.create_todo_list_func.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.create_todo_list_func.create_todo_list_util',
                create_todo_list_util
            )
        )
        result = await create_todo_list(request, title='example')

    create_todo_list_util.assert_awaited()
    assert isinstance(result, TodoList)
    assert result.id == 12
    assert result.title == 'example'
