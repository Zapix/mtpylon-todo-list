# -*- coding: utf-8 -*-
import pytest
from contextlib import ExitStack
from unittest.mock import patch, AsyncMock, MagicMock

from faker import Faker
from sqlalchemy.orm import sessionmaker

from users.models import User
from todos.utils import create_todo_list, get_todo_lists


@pytest.mark.asyncio
async def test_create_todo_list_empty(user):
    with pytest.raises(ValueError):
        await create_todo_list(user, '')


@pytest.mark.asyncio
async def test_create_todo_list_success(
    async_session: sessionmaker,
    user: User,
    fake: Faker
):
    title = fake.name()
    todo_list = MagicMock(id=1, title=title)

    dal_create_todo_list = AsyncMock(return_value=todo_list)

    with ExitStack() as patcher:
        patcher.enter_context(
            patch('todos.utils.async_session', async_session),
        )
        patcher.enter_context(
            patch('todos.utils.dal_create_todo_list', dal_create_todo_list)
        )

        returned_todo_list = await create_todo_list(user, title)

    assert returned_todo_list.id == todo_list.id
    assert returned_todo_list.title == todo_list.title


@pytest.mark.asyncio
async def test_get_todo_lists(
    async_session: sessionmaker,
    user: User,
    fake: Faker,
):
    todo_lists = [MagicMock(id=(x + 1), title=fake.name()) for x in range(15)]
    dal_get_todo_lists = AsyncMock(return_value=todo_lists)

    with ExitStack() as patcher:
        patcher.enter_context(
            patch('todos.utils.async_session', async_session),
        )
        patcher.enter_context(
            patch('todos.utils.dal_get_todo_lists', dal_get_todo_lists)
        )

        returned_todo_lists = await get_todo_lists(user)

    assert len(returned_todo_lists) == 15
    dal_get_todo_lists.assert_awaited()