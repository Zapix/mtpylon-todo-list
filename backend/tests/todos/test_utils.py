# -*- coding: utf-8 -*-
import pytest
from contextlib import ExitStack
from unittest.mock import patch, AsyncMock, MagicMock

from faker import Faker
from sqlalchemy.orm import sessionmaker

from users.models import User
from todos.models import TodoList
from todos.utils import (
    create_todo_list,
    get_todo_lists,
    get_todo_list_for_user,
    delete_todo_list,
    create_task,
    get_tasks_for_todo_list,
    get_task_for_user,
    change_title,
    mark_completed,
)


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


@pytest.mark.asyncio
async def test_get_todo_list_for_user_none(
    async_session: sessionmaker,
    user: User,
):
    dal_get_single_todo_list = AsyncMock(return_value=None)

    with ExitStack() as patcher:
        patcher.enter_context(
            patch('todos.utils.async_session', async_session)
        )
        patcher.enter_context(
            patch(
                'todos.utils.dal_get_single_todo_list',
                dal_get_single_todo_list
            )
        )

        returned_todo_list = await get_todo_list_for_user(user, 12)

    assert returned_todo_list is None
    dal_get_single_todo_list.assert_awaited()


@pytest.mark.asyncio
async def test_get_todo_list_for_user_real_item(
    async_session: sessionmaker,
    user: User,
    fake: Faker,
):
    todo_list = MagicMock(id=12, title=fake.name())
    dal_get_single_todo_list = AsyncMock(return_value=todo_list)

    with ExitStack() as patcher:
        patcher.enter_context(
            patch('todos.utils.async_session', async_session)
        )
        patcher.enter_context(
            patch(
                'todos.utils.dal_get_single_todo_list',
                dal_get_single_todo_list
            )
        )

        returned_todo_list = await get_todo_list_for_user(user, 12)

    assert returned_todo_list is not None
    assert returned_todo_list.id == 12
    dal_get_single_todo_list.assert_awaited()


@pytest.mark.asyncio
async def test_delete_todo_list(async_session: sessionmaker):
    todo_list = MagicMock(id=43, title='sample')
    dal_delete_todo_list = AsyncMock()

    with ExitStack() as patcher:
        patcher.enter_context(
            patch('todos.utils.async_session', async_session)
        )
        patcher.enter_context(
            patch('todos.utils.dal_delete_todo_list', dal_delete_todo_list)
        )

        await delete_todo_list(todo_list)

    dal_delete_todo_list.assert_awaited()


@pytest.mark.asyncio
async def test_create_task(async_session: sessionmaker, todo_list: TodoList):
    task = MagicMock(id=12, title='first task', todo_list=todo_list)

    dal_create_task = AsyncMock(return_value=task)

    with ExitStack() as patcher:
        patcher.enter_context(
            patch('todos.utils.async_session', async_session)
        )
        patcher.enter_context(
            patch('todos.utils.dal_create_task', dal_create_task)
        )

        new_task = await create_task(todo_list, 'first task')

    assert new_task == task


@pytest.mark.asyncio
async def test_get_tasks_for_todo_list(
    async_session: sessionmaker,
    fake: Faker,
    todo_list: TodoList
):
    tasks = [
        MagicMock(id=(x + 1), title=fake.name(), todo_list=todo_list)
        for x in range(15)
    ]
    dal_get_task_list = AsyncMock(return_value=tasks)

    with ExitStack() as patcher:
        patcher.enter_context(
            patch('todos.utils.async_session', async_session)
        )
        patcher.enter_context(
            patch('todos.utils.dal_get_task_list', dal_get_task_list)
        )

        retrieved_tasks = await get_tasks_for_todo_list(todo_list)

    assert len(retrieved_tasks) == 15


@pytest.mark.asyncio
async def test_get_task_for_user_ok(
    async_session: sessionmaker,
    fake: Faker,
    user: User
):
    task = MagicMock(id=32, title=fake.name())
    dal_get_task = AsyncMock(return_value=task)

    with ExitStack() as patcher:
        patcher.enter_context(
            patch('todos.utils.async_session', async_session)
        )
        patcher.enter_context(
            patch('todos.utils.dal_get_task', dal_get_task)
        )

        retrieved_task = await get_task_for_user(user, 32)

    assert retrieved_task == task


@pytest.mark.asyncio
async def test_get_task_for_user_none(
    async_session: sessionmaker,
    user: User
):
    dal_get_task = AsyncMock(return_value=None)

    with ExitStack() as patcher:
        patcher.enter_context(
            patch('todos.utils.async_session', async_session)
        )
        patcher.enter_context(
            patch('todos.utils.dal_get_task', dal_get_task)
        )

        retrieved_task = await get_task_for_user(user, 43)

    assert retrieved_task is None


@pytest.mark.asyncio
async def test_change_title(
    async_session: sessionmaker,
    fake: Faker
):
    task = MagicMock(id=12, title=fake.name())

    updated_task = MagicMock(id=12, title='new_title')
    dal_update_task = AsyncMock(return_value=updated_task)

    with ExitStack() as patcher:
        patcher.enter_context(
            patch('todos.utils.async_session', async_session)
        )
        patcher.enter_context(
            patch('todos.utils.dal_update_task', dal_update_task)
        )

        handled_task = await change_title(task, 'new_title')

    assert updated_task == handled_task
    dal_update_task.assert_awaited()


@pytest.mark.asyncio
async def test_mark_completed(
    async_session: sessionmaker,
    fake: Faker
):
    task = MagicMock(id=12, title=fake.name(), completed=False)

    updated_task = MagicMock(12, title=task.title, completed=True)
    dal_update_task = AsyncMock(return_value=updated_task)

    with ExitStack() as patcher:
        patcher.enter_context(
            patch('todos.utils.async_session', async_session)
        )
        patcher.enter_context(
            patch('todos.utils.dal_update_task', dal_update_task)
        )
        completed_task = await mark_completed(task)

    assert completed_task == updated_task
    dal_update_task.assert_awaited()
