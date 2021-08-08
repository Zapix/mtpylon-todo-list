# -*- coding: utf-8 -*-
import pytest
from contextlib import ExitStack
from unittest.mock import AsyncMock, MagicMock, patch

from mtpylon.exceptions import RpcCallError
from mtpylon.contextvars import auth_key_var
from mtpylon.crypto.auth_key import AuthKey

from schema.constructors import BoolTrue
from schema.functions.remove_todo_list_func import remove_todo_list
from users.models import User


@pytest.mark.asyncio
async def test_remove_todo_list_404(
    user: User,
    mtpylon_auth_key: AuthKey,
):
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)

    request = MagicMock()

    get_todo_list_for_user = AsyncMock(return_value=None)

    delete_todo_list = AsyncMock()

    with ExitStack() as patcher:
        patcher.enter_context(
            patch(
                'schema.utils.decorators.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.remove_todo_list_func.'
                'get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.'
                'remove_todo_list_func.'
                'get_todo_list_for_user',
                get_todo_list_for_user
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.remove_todo_list_func.delete_todo_list',
                delete_todo_list
            )
        )

        with pytest.raises(RpcCallError):
            await remove_todo_list(request, todo_list_id=32)

    delete_todo_list.assert_not_awaited()


@pytest.mark.asyncio
async def test_remove_todo_list_success(
    user: User,
    mtpylon_auth_key: AuthKey
):
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)

    request = MagicMock()

    todo_list = MagicMock(id=32, title='main')
    get_todo_list_for_user = AsyncMock(return_value=todo_list)

    delete_todo_list = AsyncMock()

    with ExitStack() as patcher:
        patcher.enter_context(
            patch(
                'schema.utils.decorators.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.remove_todo_list_func.'
                'get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.'
                'remove_todo_list_func.'
                'get_todo_list_for_user',
                get_todo_list_for_user
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.remove_todo_list_func.delete_todo_list',
                delete_todo_list
            )
        )

        returned_value = await remove_todo_list(request, todo_list_id=32)

    get_todo_list_for_user.assert_awaited_with(user, 32)
    assert isinstance(returned_value, BoolTrue)

    delete_todo_list.assert_awaited()
