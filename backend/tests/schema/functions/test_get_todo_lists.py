# -*- coding: utf-8 -*-
import pytest
from contextlib import ExitStack
from unittest.mock import AsyncMock, MagicMock, patch
from faker import Faker
from mtpylon.contextvars import auth_key_var
from mtpylon.crypto import AuthKey


from schema.constructors import TodoList, TodoListsResult
from schema.functions.get_todo_lists_func import get_todo_lists
from users.models import User


@pytest.mark.asyncio
async def test_get_todo_lists(
    user: User,
    mtpylon_auth_key: AuthKey,
    fake: Faker
):
    auth_key_var.set(mtpylon_auth_key)
    get_user_by_auth_key = AsyncMock(return_value=user)

    todo_lists = [
        MagicMock(id=(x + 1), title=fake.name()) for x in range(13)
    ]
    get_todo_lists_util = AsyncMock(return_value=todo_lists)

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
                'schema.functions.get_todo_lists_func.get_user_by_auth_key',
                get_user_by_auth_key
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.get_todo_lists_func.get_todo_lists_util',
                get_todo_lists_util
            )
        )

        result = await get_todo_lists(request)

    assert isinstance(result, TodoListsResult)
    assert len(result.todo_lists) == 13
    assert isinstance(result.todo_lists[0], TodoList)
    get_todo_lists_util.assert_awaited()
